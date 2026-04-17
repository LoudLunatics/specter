from spectre.ui import console, show_welcome, show_status, show_success, show_error
from spectre.config import setup_config
from spectre.engine import SpectreEngine
from rich.table import Table

def main():
    show_welcome()
    
    # Inisialisasi API Key
    api_key = setup_config()
    if not api_key:
        show_error("API Key missing! Please check your config.")
        return

    engine = SpectreEngine(api_key)

    # Input Koordinat
    lat = console.input("[bold red]SPECTRE[/bold red]@[bold white]lat[/bold white]: ")
    lon = console.input("[bold red]SPECTRE[/bold red]@[bold white]lon[/bold white]: ")
    rad = console.input("[bold red]SPECTRE[/bold red]@[bold white]rad(km)[/bold white]: ")

    show_status(f"Scanning radius {rad}km from {lat}, {lon}...")

    # Proses Scan
    with console.status("[bold yellow]Triangulating signals...[/bold yellow]"):
        results = engine.search_radar(lat, lon, rad)

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
