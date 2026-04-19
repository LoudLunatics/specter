from rich.console import Console
import os

console = Console()

# ASCII Art diperbarui murni menjadi "SPECTER" (Tanpa LOC)
BANNER = r"""[bold red]
  _____ _____  ______ _____ _______ ______ _____  
 / ____|  __ \|  ____/ ____|__   __|  ____|  __ \ 
| (___ | |__) | |__ | |       | |  | |__  | |__) |
 \___ \|  ___/|  __|| |       | |  |  __| |  _  / 
 ____) | |    | |___| |____   | |  | |____| | \ \ 
|_____/|_|    |______\_____|  |_|  |______|_|  \_\
[/bold red]
[bold white]        >> NETWORK RECONNAISSANCE & INFILTRATION ENGINE <<[/bold white]
"""

def show_welcome():
    # Membersihkan layar terminal sebelum mencetak banner
    os.system('clear' if os.name == 'posix' else 'cls')
    console.print(BANNER)
    console.print("[dim]Version 1.2.0 | Authorized Red Team Access Only[/dim]")
    console.print("[bold red]—[/bold red]" * 70)

def show_status(msg):
    console.print(f"[bold yellow][*][/bold yellow] {msg}")

def show_success(msg):
    console.print(f"[bold green][+][/bold green] {msg}")

def show_error(msg):
    console.print(f"[bold red][!][/bold red] {msg}")
