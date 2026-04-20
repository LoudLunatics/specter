# 📡 SPECTRE-LOC: Geolocation Recon Engine

> ⚠️ ARCH LINUX EXCLUSIVE
> *This tool is strictly built and optimized for Arch Linux and its derivatives (EndeavourOS, Manjaro, BlackArch). It leverages the pacman package manager and PEP 517 build standards. Execution on Debian, Ubuntu, Windows, or macOS is explicitly locked and not supported.*

SPECTRE-LOC is an advanced Open-Source Intelligence (OSINT) terminal interface designed to triangulate and map exposed IoT devices (such as IP cameras, RTSP streams, and web servers) within a specific geographic radius using the Shodan API.

## ⚙️ Tech Stack
- Language: Python 3.12+
- Build System: PEP 517 (python-build, python-installer, wheel)
- Core Engine: Shodan API 
- UI Framework: Rich (Terminal Formatting)

## 🚀 Key Features
- OS-Level Locking: Enforces Arch Linux execution to ensure compatibility with native networking toolchains.
- Geofencing Triangulation: Pinpoint exposed devices within a 1-20km radius of a specific latitude/longitude.
- Persistent Configuration: Automatically securely stores API credentials in ~/.config/spectre-loc/ natively conforming to XDG Base Directory Specification.
- Rich Terminal UI: Tactical, color-coded terminal output using Rich for rapid data parsing during active reconnaissance.
- Multi-Language Builds: Supports PKGBUILD distribution in multiple localized formats (ID, EN, JP, CN) via the pkgbuilds/ directory.

---

## 🛠 Installation (The Arch Way)

Ensure your system has the base development tools and an AUR helper (like yay) installed.

1. Clone the repository
```bash
git clone [https://github.com/yourusername/spectre-loc.git](https://github.com/yourusername/spectre-loc.git)
cd spectre-loc

2. Install external dependencies via AUR
Bash

yay -S --needed python-dotenv python-rich python-shodan

3. Build and Install via makepkg
Bash

makepkg -si

💻 Usage

Once installed globally, you can invoke the engine from any directory:
Bash

spectre-loc

First-Run Setup

On the first execution, SPECTRE-LOC will prompt you for your Shodan API Key. It will be securely stored in ~/.config/spectre-loc/.env and will not be requested again.
Example Output
Plaintext

   _____ ____  _________________  ______       ____  ______
  / ___//  \/ ____/ ____/_  /  \   / /   /  \/ ____/
  \ \/ /_/ / __/ / /     / / / /_/ /  / /   / / / / /     
 ___/ / ____/ /___/ /___  / / / _, _/  / /___/ /_/ / /___   
/____/_/   /_____/\____/ /_/ /_/ |_|  /_____/\____/\____/   

        >> GEOLOCATION SURVEILLANCE & RECON ENGINE <<
Version 1.0.0 | Authorized Red Team Access Only
——————————————————————————————————————————————————————————————

SPECTRE@lat: -6.2146
SPECTRE@lon: 106.8451
SPECTRE@rad(km): 15

[*] Scanning radius 15km from -6.2146, 106.8451...
⠧ Triangulating signals...

TARGETS ACQUIRED (5 found)
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┓
┃ IP Address      ┃ Organization              ┃ Port ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━┩
│ 103.144.xxx.xx  │ PT. Telkom Indonesia      │  554 │
│ 114.122.xxx.xx  │ Biznet Networks           │  554 │
│ 36.68.xxx.xx    │ PT. Supra Primatama       │  554 │
│ 180.250.xxx.xx  │ MyRepublic Broadband      │ 8080 │
│ 202.169.xxx.xx  │ PT. Indosat Tbk           │   80 │
└─────────────────┴───────────────────────────┴──────┘

[+] Reconnaissance complete.

🌍 Localization (Multi-Language Builds)

SPECTRE-LOC supports localized Arch Linux package descriptions for international Red Team operators. The default PKGBUILD is in English, but localized versions are available in the pkgbuilds/ directory.

Supported languages:

    ID : Indonesian (Bahasa Indonesia)

    JP : Japanese (日本語)

    CN : Chinese (中文)

How to build with a localized package description:
If you want to install SPECTRE-LOC using the Japanese package description, simply overwrite the default PKGBUILD before compiling:
Bash

# 1. Copy the desired language PKGBUILD to the root directory
cp pkgbuilds/PKGBUILD.jp PKGBUILD

# 2. Build and install as usual
makepkg -si

Note: The core CLI engine will remain in English to maintain syntax consistency across global environments.
🛡 Disclaimer

This project is developed strictly for educational purposes and ethical security research. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Always adhere to local cybersecurity laws and obtain proper authorization before scanning networks you do not own.