import shutil
import sys
from specter.ui import console, show_status, show_success, show_error

def setup_config():
    """
    Pre-Flight Check: Memastikan semua dependensi sistem tersedia 
    sebelum engine dijalankan.
    """
    # Cek apakah aplikasi Nmap ada di dalam sistem Linux
    if shutil.which("nmap") is None:
        show_error("CRITICAL ENGINE FAILURE: Nmap is not installed!")
        console.print("Please install Nmap on your Arch/EndeavourOS system using:")
        console.print("[bold yellow]sudo pacman -S nmap[/bold yellow]\n")
        sys.exit(1) # Hentikan program jika Nmap tidak ada
        
    return True # Kembalikan sinyal hijau jika mesin siap