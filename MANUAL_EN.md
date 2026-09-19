# KiCad AI PCB Copilot & Auto-Router — User Manual & Technical Guide

---

## 1. Overview & System Architecture

**KiCad AI PCB Copilot & Auto-Router** is an intelligent, physics-informed layout and routing acceleration suite for KiCad 7.x and KiCad 8.x (`pcbnew`).

### Core Design Philosophy: "Component Placement Invariance"
Unlike naive autorouters that scramble human-placed footprints, the Copilot respects your manual component placement:
- **Zero Component Displacement**: Your microcontrollers, RF connectors, crystal oscillators, and bypass capacitors stay precisely where you placed them.
- **Physics-Informed Routing**: Traces, vias, copper pours, and ground connections are automatically routed and sized according to IPC-2152 thermal rules, 50Ω RF coplanar waveguide equations, and star net-tie grounding principles.

---

## 2. Key Capabilities & Technical Features

| Feature | Engineering Formulation | KiCad Implementation |
| :--- | :--- | :--- |
| **Board Setup Synchronization** | Live sync of PCB Thickness ($0.6\text{–}3.2\text{ mm}$), Copper Weight ($0.5\text{–}3.0\text{ oz}$), and Clearances | Applied to `board.GetDesignSettings()` and `.kicad_pcb` setup |
| **IPC-2152 High-Current Power Routing** | $I = k \cdot \Delta T^{0.44} \cdot A^{0.725}$ | Auto-calculated wide power traces (12V, 24V, Motor) with $45^\circ$ mitered bends |
| **50Ω RF Coplanar Waveguide (CPWG)** | Conformal mapping calculation for $W$ (width) and $S$ (spacing) based on $\varepsilon_r$ and dielectric height | Guard ground traces with $\lambda/20$ stitching via fences around RF antennas |
| **Antenna Keepout Zone** | 3D radiation boundary ($12\times 8\text{ mm}$) | Negative keepout on all copper layers preventing ground noise beneath chip antennas |
| **Analog / Digital Star Net-Tie** | Single-point junction topology | Merges `GNDA` and `GND` at a designated star net-tie without ground loop EMI |
| **Crystal Oscillator Isolation** | Guard ring & keepout boundary | Isolates sensitive high-frequency crystal routing from switching regulator noise |
| **Differential Pair Skew Equalization** | Phase matched to $\le 0.1\text{ mm}$ skew | Serpentine length-matching accordions on high-speed USB D+/D- lines |
| **Thermal Dissipation Matrices** | Low thermal resistance via grid ($R_{th} < 12^\circ\text{C/W}$) | Multi-via heatsink arrays stitched beneath power MOSFETs and DC-DC converters |

---

## 3. Installation Methods

### Method 1: KiCad PCM (Plugin & Content Manager) — Recommended
1. Open **KiCad** (or the **PCB Editor** `pcbnew`).
2. Click on the **Plugin and Content Manager (PCM)** icon on the top toolbar or main window.
3. At the bottom of the PCM window, click **"Install from File..."**.
4. Select the `kicad-ai-copilot-plugin.zip` file.
5. KiCad will validate the package schema (`metadata.json`). Click **"Apply Changes"**.
6. The plugin icon will now appear in the PCB Editor top toolbar!

---

### Method 2: 1-Click Automated Script
Extract the archive and run the corresponding script:
- **Windows**: Double-click `install_windows.bat`. It detects `%APPDATA%\kicad\8.0\` or `7.0\` and copies the plugin files automatically.
- **Linux & macOS**: Open terminal and execute:
  ```bash
  bash install_linux_mac.sh
  ```

---

### Method 3: Manual Installation
Copy the contents of the `plugins/` directory into your KiCad scripting folder:
- **Windows**: `%APPDATA%\kicad\8.0\scripting\plugins\kicad_ai_copilot\`
- **Linux**: `~/.local/share/kicad/8.0/scripting/plugins/kicad_ai_copilot/`
- **macOS**: `~/Library/Application Support/kicad/8.0/scripting/plugins/kicad_ai_copilot/`

Then inside KiCad PCB Editor, click:  
**Tools -> External Plugins -> Refresh Plugins**.

---

## 4. How to Use the Plugin

1. **Place Your Footprints**: Place all ICs, connectors, passives, and antennas in KiCad as usual.
2. **Launch the Copilot**:
   - Click the **KiCad AI Copilot** button on the top toolbar, or go to **Tools -> External Plugins -> KiCad AI PCB Copilot & Auto-Router**.
3. **Automated 4-Cycle Execution**:
   - **Cycle 1**: Net & differential pair classification, design rules initialization.
   - **Cycle 2**: IPC-2152 power trace sizing, $45^\circ$ mitered corners.
   - **Cycle 3**: RF 50Ω CPWG calculation, via fence generation, Star Net-Tie creation.
   - **Cycle 4**: Serpentine skew tuning and thermal dissipation via stitching.
4. **Run KiCad DRC**:
   - Run the built-in **Design Rules Checker (DRC)** in KiCad to confirm zero clearance, spacing, or differential errors.

---

## 5. Technical Specifications & Defaults

- **Supported KiCad Versions**: KiCad 7.0.0+ and KiCad 8.0.0+
- **API Runtime**: Python 3 with native `pcbnew` module
- **Default Stackup**: 4-Layer FR-4 ($\varepsilon_r = 4.5$, $1.6\text{ mm}$ thickness, $1.0\text{ oz}$ outer copper)
- **Annular Ring Safety Margin**: Minimum annular ring $[(\text{Pad} - \text{Drill})/2] \ge 0.125\text{ mm}$ ($5\text{ mil}$) enforced.
