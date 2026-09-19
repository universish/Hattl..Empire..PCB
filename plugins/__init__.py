# -*- coding: utf-8 -*-
"""
KiCad AI PCB Copilot & Auto-Router
ActionPlugin Registration Module (KiCad 7.x & 8.x pcbnew API)
"""

import os
import sys

current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from .kicad_ai_copilot import KiCadAiCopilotPlugin
    KiCadAiCopilotPlugin().register()
except Exception as err:
    try:
        import pcbnew
        pcbnew.wxLogMessage(f"[KiCad AI Copilot] Plugin registration error: {err}")
    except Exception:
        print(f"[KiCad AI Copilot] Plugin registration error: {err}")
