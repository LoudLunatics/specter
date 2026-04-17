from spectre.ui import console, show_welcome, show_status, show_success, show_error
from spectre.engine import SpectreEngine
from rich.table import Table

def main():
    show_welcome()
    
    # Input target sekarang berupa IP atau Range
    target = console.input("[bold red]SPECTRE[/bold red]@[bold white]target_ip/range[/bold white]: ")
    
    # Fitur baru: Pilih Mode
    mode = console.input("[bold red]SPECTRE[/bold red]@[bold white]stealth_mode(y/n)[/bold white]: ").lower()
    is_stealth = True if mode == 'y' else False

    show_status(f"Scanning target {target} in {'GHOST' if is_stealth else 'NORMAL'} mode...")

    engine = SpectreEngine()
    
    # Proses Scan
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
            table.add_row(match['ip_str'], match.get('org', 'Unknown')[:25], str(match['port']))

        console.print("\n", table)
        show_success("Reconnaissance complete.")
    else:
        show_error(f"Engine Failure: {results}")

if __name__ == "__main__":
    main()
