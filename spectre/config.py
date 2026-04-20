import os
from pathlib import Path
from dotenv import set_key, load_dotenv
from spectre.ui import console, show_status, show_success

CONFIG_DIR = Path.home() / ".config" / "spectre-loc"
ENV_FILE = CONFIG_DIR / ".env"

def setup_config():
    # Buat folder ~/.config/spectre-loc jika belum ada
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True)
    
    # Jika file .env belum ada, minta user masukkan API Key
    if not ENV_FILE.exists():
        show_status("First time setup detected. Configuring system...")
        api_key = console.input("[bold cyan]Enter your Shodan API Key: [/bold cyan]")
        ENV_FILE.touch()
        set_key(str(ENV_FILE), "SHODAN_API_KEY", api_key)
        show_success(f"API Key saved securely to {ENV_FILE}")
        console.print("—" * 62)

    # Load API Key ke environment
    load_dotenv(ENV_FILE)
    return os.getenv("SHODAN_API_KEY")