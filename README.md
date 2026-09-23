# KiCad AI PCB Copilot & Auto-Router

[![KiCad Version](https://img.shields.io/badge/KiCad-10.0.6+-blue.svg)](https://kicad.org)
[![Rust](https://img.shields.io/badge/Rust-High%20Performance-orange.svg)](https://rust-lang.org)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://python.org)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![IPC Standard](https://img.shields.io/badge/Standard-IPC--2152-orange.svg)](https://ipc.org)
[![Platform](https://img.shields.io/badge/Platform-Fedora%2044%20%7C%20Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()
[![Build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)]()
[![Main Repo](https://img.shields.io/badge/codeberg-Repo-blue?logo=codeberg)](https://codeberg.org/universish/Hattl..Empire..PCB)
[![Mirror Repo](https://img.shields.io/badge/github-Mirror%20repo-blue?logo=github)](https://github.com/universish/Hattl..Empire..PCB/)

---

<img width="2140" height="1984" alt="hittite-logo" src="https://github.com/user-attachments/assets/786e7e4f-b78d-46e0-bfed-a65005e572c9" />


---

> **Physics-informed, AI-accelerated routing and layout copilot for KiCad EDA, powered by a high-performance Rust engine.**
> Optimized for Linux distributions (like Fedora 44) with AVX2 CPU and modern hardware awareness.
> Maintains 100% human component placement while automating IPC-2152 power traces, 50Ω RF Coplanar Waveguides (CPWG), Star Net-Ties, and high-speed serpentine skew matching.

Hittites /ˈhɪtaɪts/ 

Hittite Empire (KUR URU.ḪattI)

Hattusa Ḫa-at-tu-ša Hattusha 
Tarḫuntašša 
Šamuḫa 

Language: Hittite, Hattic, Luwian, Hurrian 

See: [wikipedia](https://en.wikipedia.org/wiki/Hittites)


Physics-informed, AI-accelerated routing and layout copilot for KiCad EDA, powered by a high-performance Rust engine 
KiCAD Plugin

---

## Highlights

- **Component Placement Invariance**: Never moves your footprints or connectors.
- **Dynamic Board Setup Sync**: Direct control over PCB Board Thickness ($0.6\text{–}3.2\text{ mm}$), Copper Weight ($0.5\text{–}3.0\text{ oz}$), and Clearances.
- **IPC-2152 Power Sizing**: Current-density routing for high current nets ($I = k \cdot \Delta T^{0.44} \cdot A^{0.725}$) with $45^\circ$ mitered bends.
- **RF 50Ω CPWG & Via Fence**: Grounded coplanar waveguide impedance calculation with $\lambda/20$ stitching via shielding.
- **Star Net-Tie Junction**: Merges analog (`GNDA`) and digital (`GND`) at a single net-tie point to prevent ground loops.
- **Crystal Keepout Guard Ring**: Eliminates capacitive and switching noise near sensitive clock oscillators.
- **Serpentine Differential Skew Tuning**: Phase matches high-speed pairs (USB / Ethernet) within $\le 0.1\text{ mm}$.
- **Thermal Heatsink Matrices**: Automated low-impedance thermal via stitching under power ICs.

---

## Quick Installation

### Method 1: KiCad PCM (Recommended)
1. Open **KiCad** -> Click **Plugin and Content Manager (PCM)**.
2. Click **Install from File...** at the bottom.
3. Select `kicad-ai-copilot-plugin.zip`.
4. Click **Apply Changes**.

### Method 2: 1-Click Script
- **Windows**: Run `install_windows.bat`
- **Linux & macOS**: Run `bash install_linux_mac.sh`

For detailed step-by-step instructions, see **[MANUAL_EN.md](MANUAL_EN.md)** or **[KURULUM_KILAVUZU_TR.txt](KURULUM_KILAVUZU_TR.txt)**.

---

## Repository Structure

```text
├── .gitignore               # Clean git tracking rules for KiCad & Python
├── metadata.json            # Official KiCad PCM schema v1
├── README.md                # This file
├── MANUAL_EN.md             # Complete English User Manual & Technical Guide
├── KURULUM_KILAVUZU_TR.txt  # Turkish Installation and Usage Guide
├── COPYRIGHT.md             # Copyright and Intellectual Property Notice
├── EULA.md                  # Commercial End User License Agreement (Web Platform)
├── NOTICES.md               # Third-party software & engineering standards acknowledgments
├── install_windows.bat      # 1-Click Windows installer
├── install_linux_mac.sh     # 1-Click Linux / macOS installer
├── resources/
│   └── icon.png             # PCM package badge icon (64x64)
└── plugins/
    ├── __init__.py          # KiCad ActionPlugin registration entry
    ├── kicad_ai_copilot.py  # Production Python routing engine
    └── icon.png             # PCB Editor toolbar icon
```

---

## Licensing & Intellectual Property

This project operates under a **Dual-Architecture & Dual-Licensing Model**:
- **KiCad Desktop Plugin (`plugins/`)**: Distributed under the **GNU General Public License v3.0 (GPLv3)** for full compatibility with the KiCad ecosystem.
- **Commercial Web SaaS & Cloud Routing Engine**: **Proprietary & Closed-Source (All Rights Reserved by Saffet Yavuz)**. The web platform, AI routing heuristics, and cloud backend are strictly excluded from the GPL under network isolation terms.

For full legal terms, consult **[COPYRIGHT.md](COPYRIGHT.md)**, **[EULA.md](EULA.md)**, and **[NOTICES.md](NOTICES.md)**.
