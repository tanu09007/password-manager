from manager import PasswordManager
from auth import setup_master_password, verify_master_password, check_master_password_exists
from generator import generate_password
from strength import check_strength
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def print_menu():
    console.print(Panel.fit(
        "[bold cyan]🔐 Password Manager[/bold cyan]",
        border_style="cyan"
    ))
    console.print("[bold white]1.[/bold white] Add password")
    console.print("[bold white]2.[/bold white] Get password")
    console.print("[bold white]3.[/bold white] List all sites")
    console.print("[bold white]4.[/bold white] Delete password")
    console.print("[bold white]5.[/bold white] Generate random password")
    console.print("[bold white]6.[/bold white] Exit")

def main():
    # Master password check
    if not check_master_password_exists():
        setup_master_password()

    if not verify_master_password():
        return

    pm = PasswordManager()

    while True:
        print_menu()
        choice = console.input("\n[bold yellow]Enter choice: [/bold yellow]")

        if choice == "1":
            site = console.input("[cyan]Enter site: [/cyan]")
            if site.strip() == "":
                console.print("[red]❌ Site name cannot be empty![/red]")
            else:
                username = console.input("[cyan]Enter username: [/cyan]")
                console.print("[dim]Leave blank to generate a random password[/dim]")
                password = console.input("[cyan]Enter password: [/cyan]")

                if password == "":
                    password = generate_password()
                    console.print(f"[green]🎲 Generated password: {password}[/green]")

                strength, feedback = check_strength(password)
                console.print(f"\nPassword Strength: {strength}")
                if feedback:
                    console.print("[yellow]Suggestions:[/yellow]")
                    for tip in feedback:
                        console.print(f"  {tip}")

                pm.add_password(site, username, password)

        elif choice == "2":
            site = console.input("[cyan]Enter site: [/cyan]")
            try:
                result = pm.get_password(site)
                if result:
                    table = Table(title=f"🔑 {site}")
                    table.add_column("Field", style="cyan")
                    table.add_column("Value", style="green")
                    table.add_row("Username", result['username'])
                    table.add_row("Password", result['password'])
                    console.print(table)
            except Exception as e:
                console.print(f"[red]❌ Something went wrong: {e}[/red]")

        elif choice == "3":
            if not pm.passwords:
                console.print("[red]No passwords saved yet.[/red]")
            else:
                table = Table(title="📋 Saved Sites")
                table.add_column("No.", style="cyan")
                table.add_column("Site", style="green")
                for i, site in enumerate(pm.passwords, 1):
                    table.add_row(str(i), site)
                console.print(table)

        elif choice == "4":
            site = console.input("[cyan]Enter site: [/cyan]")
            pm.delete_password(site)

        elif choice == "5":
            length = console.input("[cyan]Enter password length (default 12): [/cyan]")
            try:
                length = int(length) if length else 12
                if length < 6:
                    console.print("[red]❌ Password length must be at least 6![/red]")
                else:
                    password = generate_password(length)
                    console.print(f"[green]🎲 Generated password: {password}[/green]")
            except ValueError:
                console.print("[red]❌ Please enter a valid number![/red]")

        elif choice == "6":
            console.print("[bold green]👋 Bye![/bold green]")
            break

        else:
            console.print("[red]❌ Invalid choice! Enter 1-6[/red]")

main()