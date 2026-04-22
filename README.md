# 📡 SPECTER: Ghost Network Recon Engine

> ⚠️ ARCH LINUX EXCLUSIVE
> *This tool is strictly built and optimized for Arch Linux and its derivatives (EndeavourOS, Manjaro, BlackArch). It leverages the pacman package manager and PEP 517 build standards. Execution on Debian, Ubuntu, Windows, or macOS is explicitly locked and not supported.*

**SPECTER** is an advanced, standalone network reconnaissance terminal interface. Powered by `nmap` under the hood, it is designed to infiltrate specific IP ranges or subnets, scanning for exposed devices (specifically targeting RTSP streams/Port 554) using tactical Stealth SYN or standard Connect scans.

## ⚙️ Tech Stack
- **Language:** Python 3.12+
- **Build System:** PEP 517 (`python-build`, `python-installer`, `wheel`)
- **Core Engine:** Nmap (Direct Local Execution via `subprocess`)
- **UI Framework:** Rich (Terminal Formatting)

## 🚀 Key Features
- **OS-Level Locking:** Enforces Arch Linux execution to ensure compatibility with native networking toolchains and Pacman dependencies.
- **100% Local Execution:** No cloud APIs, no rate limits, no API keys. All reconnaissance is strictly run using your machine's computing power.
- **Stealth Capabilities:** Choose between standard Connect Scans (`-sT`) or Ghost/Stealth SYN Scans (`-sS`) to bypass basic firewall logging.
- **Pre-Flight System Check:** Automatically verifies the presence of native system dependencies (Nmap) before allowing engine ignition.
- **Rich Terminal UI:** Tactical, color-coded terminal output for rapid data parsing during active reconnaissance.
- **Multi-Language Builds:** Supports PKGBUILD distribution in multiple localized formats (ID, EN, JP, CN) via the `pkgbuilds/` directory.

---

## 🛠 Installation (The Arch Way)

Ensure your system has the base development tools and an AUR helper (like `yay`) installed.

```bash
1. **Clone the repository**

git clone [https://github.com/yourusername/specter.git](https://github.com/yourusername/specter.git)
cd specter

    Build and Install via makepkg
    The PKGBUILD file will automatically resolve and install necessary Python libraries and system binaries (like Nmap) using Pacman.

Bash

makepkg -si

💻 Usage

Because SPECTER relies on low-level packet manipulation for Nmap's Stealth (SYN) scanning capabilities, it must be executed with root privileges.

Invoke the engine from your home or root directory:
Bash

sudo specter

Example Output
Plaintext

   _____ ____  ____________________________ 
  / ___// __ \/ ____/ ____/__  __/ ____/ __ \
  \__ \/ /_/ / __/ / /      / / / __/ / /_/ /
 ___/ / ____/ /___/ /___   / / / /___/ _, _/ 
/____/_/   /_____/\____/  /_/ /_____/_/ |_|  

      >> GEOLOCATION SURVEILLANCE & RECON ENGINE <<
Version 1.2.0 | Authorized Red Team Access Only
————————————————————————————————————————————————————————————

SPECTER@target_ip_or_range: 192.168.1.0/24
SPECTER@stealth_mode(y/n): y

[*] Scanning target 192.168.1.0/24 in GHOST (SYN) mode...
⠧ Infiltrating network...

TARGETS ACQUIRED (3 found)
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┓
┃ IP Address       ┃ Organization              ┃ Port ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━┩
│ 192.168.1.15     │ Local/Direct Target       │  554 │
│ 192.168.1.22     │ Local/Direct Target       │  554 │
│ 192.168.1.104    │ Local/Direct Target       │  554 │
└──────────────────┴───────────────────────────┴──────┘

[+] Reconnaissance complete.

🌍 Localization (Multi-Language Builds)

SPECTER supports localized Arch Linux package descriptions for international Red Team operators. The default PKGBUILD is in English, but localized versions are available in the pkgbuilds/ directory.

Supported languages:

    ID: Indonesian (Bahasa Indonesia)

    JP: Japanese (日本語)

    CN: Chinese (中文)

How to build with a localized package description:
If you want to install SPECTER using the Japanese package description, simply overwrite the default PKGBUILD before compiling:
Bash

# 1. Copy the desired language PKGBUILD to the root directory
cp pkgbuilds/PKGBUILD.jp PKGBUILD

# 2. Build and install as usual
makepkg -si

Note: The core CLI engine will remain in English to maintain syntax consistency across global environments.
🛡 Disclaimer

This project is developed strictly for educational purposes and ethical security research. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Always adhere to local cybersecurity laws and obtain proper authorization before scanning networks, IP addresses, or hardware you do not own.
