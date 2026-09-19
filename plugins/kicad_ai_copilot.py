#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KiCad AI Copilot & Auto-Router Action Plugin (KiCad 10 / High Performance)
Bridge to Rust Engine (kicad_copilot_engine)

Author: Saffet Yavuz
License: GPL-3.0-or-later (Client Plugin)
"""

import sys
import os
import json
import ctypes
import platform
import traceback

try:
    import pcbnew
except ImportError:
    pass

try:
    import wx
except ImportError:
    pass

class KiCadAiCopilotPlugin(pcbnew.ActionPlugin):
    """
    KiCad AI Copilot & Auto-Router Action Plugin - Rust Backend
    """
    def defaults(self):
        self.name = "KiCad AI PCB Copilot & Auto-Router"
        self.category = "Layout & Routing"
        self.description = "AI-Driven DRC-Aware Physics Router, Rust High-Performance Engine"
        self.show_on_toolbar = True
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        if os.path.exists(icon_path):
            self.icon_file_name = icon_path
        self.dark_icon_file_name = icon_path

    def load_rust_engine(self):
        system = platform.system().lower()
        engine_dir = os.path.join(os.path.dirname(__file__), "engine", "target", "release")

        if system == "windows":
            lib_path = os.path.join(engine_dir, "kicad_copilot_engine.dll")
        elif system == "darwin":
            lib_path = os.path.join(engine_dir, "libkicad_copilot_engine.dylib")
        else: # Linux
            lib_path = os.path.join(engine_dir, "libkicad_copilot_engine.so")

        if not os.path.exists(lib_path):
            pcbnew.wxLogMessage(f"[Error] Rust engine library not found at: {lib_path}. Please re-run install script.")
            return None

        try:
            lib = ctypes.CDLL(lib_path)
            lib.process_board_state.argtypes = [ctypes.c_char_p]
            lib.process_board_state.restype = ctypes.c_void_p
            lib.free_string.argtypes = [ctypes.c_void_p]
            return lib
        except Exception as e:
            pcbnew.wxLogMessage(f"[Error] Failed to load Rust engine: {e}")
            return None

    def extract_board_state(self, board):
        state = {
            "thickness_mm": board.GetDesignSettings().GetBoardThickness() / 1e6,
            "copper_weight_oz": 1.0, # Default
            "nets": [],
            "footprints": []
        }

        # Extract Nets
        nets = board.GetNetsByName()
        for name, net in nets.items():
            if not name:
                continue
            nc = net.GetNetClassName()

            # Simple heuristic guessing based on name
            is_analog = "A" in name.upper() or "ANA" in name.upper()
            current_a = 5.0 if "PWR" in name.upper() or "VCC" in name.upper() or "5V" in name.upper() else 0.5
            max_freq_hz = 5e9 if "RF" in name.upper() else (1e9 if "DIFF" in name.upper() else 1e6)

            state["nets"].append({
                "name": str(name),
                "net_class": str(nc),
                "is_analog": is_analog,
                "current_a": current_a,
                "max_freq_hz": max_freq_hz
            })

        # Extract Footprints
        for fp in board.GetFootprints():
            ref = fp.GetReference()
            val = fp.GetValue().lower()
            fp_type = "Generic"
            if "crystal" in val or "xtal" in val or "osc" in val:
                fp_type = "Crystal"
            elif "ant" in val:
                fp_type = "Antenna"

            pos = fp.GetPosition()
            state["footprints"].append({
                "reference": str(ref),
                "fp_type": fp_type,
                "center_x": pos.x / 1e6,
                "center_y": pos.y / 1e6
            })

        return state

    def apply_engine_commands(self, board, commands):
        settings = board.GetDesignSettings()
        net_classes = settings.GetNetClasses()

        for cmd in commands:
            ctype = cmd.get("command_type", "")
            net_name = cmd.get("net_name", "")
            params = cmd.get("params", {})

            if ctype == "SET_NETCLASS_WIDTH":
                w = params.get("width_mm", 0.25)
                nc_name = f"IPC2152_{net_name}"
                nc = net_classes.Find(nc_name)
                if not nc:
                    nc = pcbnew.NETCLASSPTR(nc_name)
                    nc.SetTrackWidth(pcbnew.FromMM(w))
                    net_classes.Add(nc)

                net = board.FindNet(net_name)
                if net:
                    net.SetNetClassName(nc_name)

            elif ctype == "ADD_KEEPOUT_GUARD_RING":
                x = params.get("x", 0.0)
                y = params.get("y", 0.0)
                r = params.get("radius_mm", 5.0)
                # Create a Keepout Zone as a guard ring (placeholder representation)
                zone = pcbnew.ZONE(board)
                # Kicad 8/10 API for zones
                # Here we just log for now to prove execution
                pass

            elif ctype == "ADD_NET_TIE":
                # Typically implies placing a footprint or bridging tracks.
                pass

            elif ctype == "TUNE_MEANDER" or ctype == "APPLY_CPWG_AND_FENCE":
                # Placeholders for advanced trace routing APIs
                pass

    def Run(self):
        try:
            board = pcbnew.GetBoard()
            if not board:
                return

            # 1. Load Rust engine
            engine_lib = self.load_rust_engine()
            if not engine_lib:
                wx.MessageBox("Rust optimization engine could not be loaded.\nDid you build it?", "Error", wx.ICON_ERROR)
                return

            # 2. Extract State
            state = self.extract_board_state(board)
            json_state = json.dumps(state).encode('utf-8')

            # 3. Call Rust Engine
            result_ptr = engine_lib.process_board_state(json_state)
            if not result_ptr:
                wx.MessageBox("Engine returned null pointer.", "Error", wx.ICON_ERROR)
                return

            result_bytes = ctypes.cast(result_ptr, ctypes.c_char_p).value
            engine_lib.free_string(result_ptr)

            result_json = json.loads(result_bytes.decode('utf-8'))

            # 4. Apply Results
            status = result_json.get("status", "ERROR")
            if status != "SUCCESS":
                wx.MessageBox(f"Engine Error: {result_json.get('message')}", "Error", wx.ICON_ERROR)
                return

            self.apply_engine_commands(board, result_json.get("commands", []))

            # Apply board thickess
            thick = result_json.get("new_board_thickness_mm", 1.6)
            board.GetDesignSettings().SetBoardThickness(pcbnew.FromMM(thick))

            pcbnew.Refresh()

            # 5. Show Real-time Feedback UI / Report
            logs = "\n".join(result_json.get("optimizations_applied", []))
            msg = f"AI Copilot & Rust Engine Finished 4-Loop Optimization:\n\n{logs}"

            if 'wx' in sys.modules:
                wx.MessageBox(msg, "Optimization Complete", wx.ICON_INFORMATION)
            else:
                pcbnew.wxLogMessage(msg)

        except Exception as e:
            err = traceback.format_exc()
            if 'wx' in sys.modules:
                wx.MessageBox(f"Exception in Python Plugin:\n{err}", "Error", wx.ICON_ERROR)
            else:
                pcbnew.wxLogMessage(f"Exception: {err}")

# Direct execution entry
if __name__ == "__main__":
    plugin = KiCadAiCopilotPlugin()
    plugin.defaults()
    plugin.Run()
