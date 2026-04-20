from specter.ui import console, show_welcome, show_status, show_success, show_error
from specter.engine import SpecterEngine
from rich.table import Table

def main():
    show_welcome()
    
    # Nmap tidak butuh API Key
    engine = SpecterEngine()

    # Input target dikembalikan ke IP atau Range
    target = console.input("[bold red]SPECTER[/bold red]@[bold white]target_ip_or_range[/bold white]: ")
    
    # Pilihan Mode Stealth
    mode = console.input("[bold red]SPECTER[/bold red]@[bold white]stealth_mode(y/n)[/bold white]: ").lower()
    is_stealth = True if mode == 'y' else False

    show_status(f"Scanning target {target} in {'GHOST (SYN)' if is_stealth else 'NORMAL'} mode...")

    # Proses Scan Nmap
    with console.status("[bold yellow]Infiltrating network...[/bold yellow]"):
        results = engine.search_radar(target, stealth_mode=is_stealth)

    # Tampilkan Hasil
    if isinstance(results, list):
        if len(results) == 0:
            show_error("No exposed devices found in this sector.")
            return

        table = Table(title=f"TARGETS ACQUIRED ({len(results)} found)", border_style="red")
        table.add_column("IP Address", justify="left", style="cyan", no_wrap=True)
        table.add_column("Organization", justify="left", style="magenta")
        table.add_column("Port", justify="center", style="yellow")

        for match in results:
            table.add_row(match['ip_str'], match.get('org', 'Unknown'), str(match['port']))

        console.print("\n", table)
        show_success("Reconnaissance complete.")
    else:
        show_error(f"Engine Failure: {results}")

if __name__ == "__main__":
    main()