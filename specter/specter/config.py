import os
from pathlib import Path
from dotenv import set_key, load_dotenv
from specter.ui import console, show_status, show_success

# Nama folder config yang benar: specter
CONFIG_DIR = Path.home() / ".config" / "specter"
ENV_FILE = CONFIG_DIR / ".env"

def setup_config():
    # Buat folder ~/.config/specter jika belum ada
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True)
    
    # Buat file .env kosong jika belum ada (untuk fitur masa depan)
    if not ENV_FILE.exists():
        ENV_FILE.touch()
        show_status("Initializing local Specter environment...")
        show_success(f"Workspace created at {CONFIG_DIR}")

    load_dotenv(ENV_FILE)
    return True
