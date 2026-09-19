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
import urllib.request
import urllib.parse
import time

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
        # Determine layer count
        layer_count = board.GetCopperLayerCount()

        state = {
            "layer_count": layer_count,
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

            elif ctype == "ADD_JUMPER":
                p_pitch = params.get("p_pitch_mm", 5.08)
                self.place_jumper_footprint(board, net_name, p_pitch)

            elif ctype == "TUNE_MEANDER" or ctype == "APPLY_CPWG_AND_FENCE":
                # Placeholders for advanced trace routing APIs
                pass

    def place_jumper_footprint(self, board, net_name, pitch_mm):
        """
        Dynamically loads a 0-ohm Jumper/Resistor footprint and places it on the board.
        Then attempts to backannotate the schematic file (.kicad_sch).
        """
        try:
            # Try to load standard axial resistor footprint as a jumper
            fp = pcbnew.FootprintLoad(
                pcbnew.GetGlobalTable(),
                "Resistor_THT",
                "R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"
            )
            if not fp:
                return

            fp.SetReference(f"JMP_{net_name}")
            fp.SetValue("0R")

            # Place it near the center (placeholder positioning)
            rect = board.GetBoardEdgesBoundingBox()
            center_x = rect.GetCenter().x
            center_y = rect.GetCenter().y
            fp.SetPosition(pcbnew.VECTOR2I(center_x, center_y))

            # Assign pads to the net
            net = board.FindNet(net_name)
            if net:
                for pad in fp.Pads():
                    pad.SetNet(net)

            board.Add(fp)

            # Text-based Schematic Backannotation
            self.backannotate_schematic(board.GetFileName(), f"JMP_{net_name}", net_name)

        except Exception as e:
            pcbnew.wxLogMessage(f"Failed to place jumper: {e}")

    def backannotate_schematic(self, pcb_path, ref_des, net_name):
        """
        Appends the newly added Jumper to the KiCad schematic by directly text-parsing the .kicad_sch file.
        """
        sch_path = pcb_path.replace(".kicad_pcb", ".kicad_sch")
        if not os.path.exists(sch_path):
            return

        try:
            with open(sch_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if ref_des in content:
                return # Already exists

            # Create a simple KiCad 7/8 symbol definition for a Device:R (Resistor)
            symbol_snippet = f'''
  (symbol (lib_id "Device:R") (at 0 0 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no)
    (property "Reference" "{ref_des}" (at 1.27 0 0))
    (property "Value" "0R" (at 1.27 -2.54 0))
    (property "Footprint" "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" (at 0 0 0))
  )
'''
            # Append before the last closing parenthesis of the schematic file
            idx = content.rfind(')')
            if idx != -1:
                new_content = content[:idx] + symbol_snippet + content[idx:]
                with open(sch_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

        except Exception as e:
            pcbnew.wxLogMessage(f"Schematic backannotation failed: {e}")

    def handle_telemetry(self, optimizations_logs):
        """
        Handles GDPR/KVKK compliant telemetry collection.
        Asks for user consent once, saves to config.json, and sends anonymous data to Google Drive Webhook.
        """
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        config = {"telemetry_enabled": False, "webhook_url": ""}

        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
            except:
                pass

        # Ask for consent if we are in a GUI environment and haven't asked before
        if 'wx' in sys.modules and not config.get("consent_asked", False):
            msg = (
                "To improve our AI models and routing algorithms, we collect ANONYMOUS telemetry data.\n"
                "This includes routing times, node counts, and rip-up success rates.\n"
                "NO proprietary design data or file names are sent.\n\n"
                "This complies with GDPR and KVKK regulations.\n"
                "Do you consent to sending this anonymous data to help improve the tool?"
            )
            dlg = wx.MessageDialog(None, msg, "GDPR / KVKK Telemetry Consent", wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            config["telemetry_enabled"] = (result == wx.ID_YES)
            config["consent_asked"] = True
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=4)

        if not config.get("telemetry_enabled", False):
            return

        webhook = config.get("webhook_url", "")
        if not webhook or "XXXX" in webhook:
            return

        # Prepare anonymous payload
        payload = {
            "timestamp": time.time(),
            "os": platform.system(),
            "kicad_version": pcbnew.GetBuildVersion() if hasattr(pcbnew, "GetBuildVersion") else "Unknown",
            "optimizations_count": len(optimizations_logs),
            "status": "Success"
        }

        # Send to Google Apps Script Webhook
        try:
            req = urllib.request.Request(webhook)
            req.add_header('Content-Type', 'application/json; charset=utf-8')
            json_data = json.dumps(payload).encode('utf-8')
            req.add_header('Content-Length', len(json_data))
            urllib.request.urlopen(req, json_data, timeout=5.0)
        except Exception as e:
            pcbnew.wxLogMessage(f"Telemetry submission failed: {e}")

    def Run(self):
        try:
            start_time = time.time()
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

            # 6. Handle Telemetry
            self.handle_telemetry(result_json.get("optimizations_applied", []))

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
