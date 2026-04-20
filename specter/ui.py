from rich.console import Console
import os

console = Console()

# Gunakan r""" (raw string) agar karakter \ tidak membuat logonya berantakan
BANNER = r"""[bold red]
   _____ ____  ____________________________ 
  / ___// __ \/ ____/ ____/__  __/ ____/ __ \
  \__ \/ /_/ / __/ / /      / / / __/ / /_/ /
 ___/ / ____/ /___/ /___   / / / /___/ _, _/ 
/____/_/   /_____/\____/  /_/ /_____/_/ |_|  
[/bold red]
[bold white]      >> GEOLOCATION SURVEILLANCE & RECON ENGINE <<[/bold white]
"""

def show_welcome():
    # Bersihkan layar sebelum menampilkan banner
    os.system('clear' if os.name == 'posix' else 'cls')
    console.print(BANNER)
    console.print("[dim]Version 1.2.0 | Authorized Red Team Access Only[/dim]")
    console.print("—" * 60)

def show_status(msg):
    console.print(f"[bold yellow][*][/bold yellow] {msg}")

def show_success(msg):
    console.print(f"[bold green][+][/bold green] {msg}")

def show_error(msg):
    console.print(f"[bold red][!][/bold red] {msg}")