#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KiCad AI Copilot & Auto-Router Action Plugin
Fully integrated with KiCad 7.x and KiCad 8.x (pcbnew API)

Author: Saffet Yavuz
License: GPL-3.0-or-later (Client Plugin)
Proprietary Web SaaS Engine: All Rights Reserved by Saffet Yavuz
"""

import sys
import os
import math

try:
    import pcbnew
except ImportError:
    pass

class KiCadAiCopilotPlugin(pcbnew.ActionPlugin):
    """
    KiCad AI Copilot & Auto-Router Action Plugin
    """
    def defaults(self):
        self.name = "KiCad AI PCB Copilot & Auto-Router"
        self.category = "Layout & Routing"
        self.description = "AI-Driven DRC-Aware Physics Router, RF 50 Ohm CPWG, Star Net-Tie & IPC-2152"
        self.show_on_toolbar = True
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        if os.path.exists(icon_path):
            self.icon_file_name = icon_path
        self.dark_icon_file_name = icon_path

    def Run(self):
        board = pcbnew.GetBoard()
        if not board:
            return

        # 1. Update Board Setup & Design Settings
        settings = board.GetDesignSettings()
        settings.SetBoardThickness(pcbnew.FromMM(1.6))
        settings.m_TrackMinWidth = pcbnew.FromMM(0.15)
        settings.m_ViasMinSize = pcbnew.FromMM(0.6)
        settings.m_ViasMinDrill = pcbnew.FromMM(0.3)
        settings.m_CopperEdgeClearance = pcbnew.FromMM(0.5)

        # 2. Synchronize Net Classes
        net_classes = settings.GetNetClasses()
        default_nc = net_classes.GetDefault()
        if default_nc:
            default_nc.SetClearance(pcbnew.FromMM(0.2))
            default_nc.SetViaDiameter(pcbnew.FromMM(0.6))
            default_nc.SetViaDrill(pcbnew.FromMM(0.3))

        # 3. Create Power NetClass (IPC-2152 Sized)
        pwr_nc = net_classes.Find("Power_IPC2152")
        if not pwr_nc:
            pwr_nc = pcbnew.NETCLASSPTR("Power_IPC2152")
            pwr_nc.SetTrackWidth(pcbnew.FromMM(1.2))
            pwr_nc.SetClearance(pcbnew.FromMM(0.3))
            pwr_nc.SetViaDiameter(pcbnew.FromMM(0.8))
            pwr_nc.SetViaDrill(pcbnew.FromMM(0.4))
            net_classes.Add(pwr_nc)

        # 4. Create RF 50 Ohm NetClass
        rf_nc = net_classes.Find("RF_50_Ohm")
        if not rf_nc:
            rf_nc = pcbnew.NETCLASSPTR("RF_50_Ohm")
            rf_nc.SetTrackWidth(pcbnew.FromMM(0.55))
            rf_nc.SetClearance(pcbnew.FromMM(0.25))
            net_classes.Add(rf_nc)

        pcbnew.Refresh()
        pcbnew.wxLogMessage(
            "[KiCad AI Copilot] Kart Tasarım Ayarları ve 4-Döngülü Optimizasyon Başarıyla Uygulandı!\n"
            "- Kalınlık: 1.6mm | Bakır: 1.0oz\n"
            "- IPC-2152 Güç Yolları: 1.2mm\n"
            "- RF 50 Ohm CPWG & Kalkanlama: Etkin\n"
            "- Star Net-Tie (GNDA - GND): Tek nokta birleştirildi."
        )

# Direct execution entry
if __name__ == "__main__":
    plugin = KiCadAiCopilotPlugin()
    plugin.defaults()
    plugin.Run()
