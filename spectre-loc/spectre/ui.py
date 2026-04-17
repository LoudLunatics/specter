from rich.console import Console
import os

console = Console()

# Perhatikan huruf 'r' di depan tanda kutip tiga untuk mencegah error escape character
BANNER = r"""[bold red]
  _____ _____  ______ _____ _______ _____  ______      _      ____   _____ 
 / ____|  __ \|  ____/ ____|__   __|  __ \|  ____|    | |    / __ \ / ____|
| (___ | |__) | |__ | |       | |  | |__) | |__ ______| |   | |  | | |     
 \___ \|  ___/|  __|| |       | |  |  _  /|  __|______| |   | |  | | |     
 ____) | |    | |___| |____   | |  | | \ \| |____     | |___| |__| | |____ 
|_____/|_|    |______\_____|  |_|  |_|  \_\______|    |______\____/ \_____|
[/bold red]
[bold white]        >> GEOLOCATION SURVEILLANCE & RECON ENGINE <<[/bold white]
"""

def show_welcome():
    # Membersihkan layar terminal sebelum mencetak banner
    os.system('clear' if os.name == 'posix' else 'cls')
    console.print(BANNER)
    console.print("[dim]Version 1.1.1 | Authorized Red Team Access Only[/dim]")
    console.print("[bold red]—[/bold red]" * 70)

def show_status(msg):
    console.print(f"[bold yellow][*][/bold yellow] {msg}")

def show_success(msg):
    console.print(f"[bold green][+][/bold green] {msg}")

def show_error(msg):
    console.print(f"[bold red][!][/bold red] {msg}")
