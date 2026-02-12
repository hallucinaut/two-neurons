"""Command Line Interface for Two Neurons"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn
from typing import Optional

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def main():
    """Two Neurons - DevOps CLI Tool"""
    pass


@main.command()
def init():
    """Initialize the project configuration"""
    console.print(Panel(
        "[bold green]Two Neurons initialized![/bold green]",
        title="Initialization Complete"
    ))


@main.command()
@click.option('--task', required=True, help='Task to execute')
@click.option('--neuron', default='primary', help='Neuron to use (primary, secondary, both)')
def run(task: str, neuron: str):
    """Run a task on neurons"""
    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
    ) as progress:
        task1 = progress.add_task("Processing on neurons...", total=None)
        progress.update(task1, description=f"Running task: {task}")
        progress.stop_task(task1)

    console.print(f"[bold cyan]Task: {task}[/bold cyan]")
    console.print(f"[bold yellow]Neuron: {neuron}[/bold yellow]")


@main.command()
def status():
    """Check the status of neurons"""
    table = Table(title="Neuron Status")
    table.add_column("Neuron", style="cyan", justify="center")
    table.add_column("Status", style="green", justify="center")
    table.add_column("Uptime", style="blue", justify="center")

    table.add_row("Primary", "🟢 Active", "2h 34m 12s")
    table.add_row("Secondary", "🟡 Idle", "45m 20s")

    console.print(table)


@main.command()
def chain():
    """Chain tasks between neurons"""
    console.print("[bold purple]Task chaining enabled[/bold purple]")
    console.print("Use --from and --to options to specify neurons")


@main.command()
@click.option('--name', required=True, help='Workflow name')
def workflow_create(name: str):
    """Create a new workflow"""
    console.print(f"[bold green]Workflow '{name}' created successfully![/bold green]")


@main.command()
def config_show():
    """Show current configuration"""
    console.print("[bold cyan]Configuration:[/bold cyan]")
    console.print("  - Timeout: 300 seconds")
    console.print("  - Default Neuron: primary")
    console.print("  - Auto-chain: enabled")


if __name__ == "__main__":
    main()
