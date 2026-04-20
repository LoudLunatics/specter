from rich.console import Console

console = Console()

BANNER = """[bold red]
   _ __  ___  __         ____
  / _//  \/ __/ /_  /  \   / /   /  \/ ____/
  \ \/ /_/ / / / /     / / / /_/ /  / /   / / / / /     
 _/ / / /_/ /_  / / / _, _/  / /_/ /_/ / /___   
/__/_/   /_/\/ /_/ /_/ |_|  /_/\/\__/   
[/bold red]
[bold white]        >> GEOLOCATION SURVEILLANCE & RECON ENGINE <<[/bold white]
"""

def show_welcome():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')
    console.print(BANNER)
    console.print("[dim]Version 1.0.0 | Authorized Red Team Access Only[/dim]")
    console.print("—" * 62)

def show_status(msg):
    console.print(f"[bold yellow][*][/bold yellow] {msg}")

def show_success(msg):
    console.print(f"[bold green][+][/bold green] {msg}")

def show_error(msg):
    console.print(f"[bold red][!][/bold red] {msg}")