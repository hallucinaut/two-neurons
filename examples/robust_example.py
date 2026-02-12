"""Robust examples showcasing Two Neurons capabilities"""

import asyncio
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

from two_neurons import (
    PrimaryNeuron,
    SecondaryNeuron,
    CustomNeuron,
    TaskExecutor,
    TaskChain,
    WorkflowManager,
)

console = Console()


async def example_1_basic_execution():
    """Example 1: Basic execution with multiple neurons"""
    console.print(Panel(
        "[bold cyan]Example 1: Basic Execution[/bold cyan]",
        title="Two Neurons Demo"
    ))

    executor = TaskExecutor()

    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
    ) as progress:
        task1 = progress.add_task("Deploying to production...", total=None)
        result1 = await executor.execute_task("deploy_service", "primary")
        progress.update(task1, description="✓ Deployment complete")

    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
    ) as progress:
        task2 = progress.add_task("Checking health...", total=None)
        result2 = await executor.execute_task("health_check", "secondary")
        progress.update(task2, description="✓ Health check passed")

    console.print(f"\n[green]✓ Deployed service: {result1['task']}[/green]")
    console.print(f"[green]✓ Health status: {result2['status']}[/green]")


async def example_2_chaining():
    """Example 2: Task chaining between neurons"""
    console.print(Panel(
        "[bold magenta]Example 2: Task Chaining[/bold magenta]",
        title="Two Neurons Demo"
    ))

    executor = TaskExecutor()

    # Create a chain: Primary → Secondary
    chain = TaskChain(executor)
    chain.add_step("primary", "analyze_logs")
    chain.add_step("secondary", "generate_report")
    chain.add_step("primary", "patch_vulnerabilities")

    console.print("\n[chocolate]Executing chain...[/chocolate]")
    console.print(f"[dim]Steps: {len(chain.chain_steps)}[/dim]\n")

    results = await chain.execute_chain()

    console.print("\n[bold cyan]Chain Results:[/bold cyan]")
    for i, result in enumerate(results, 1):
        console.print(f"  Step {i}: {result['task']} → {result['status']}")


async def example_3_workflow():
    """Example 3: Complete workflow with multiple steps"""
    console.print(Panel(
        "[bold yellow]Example 3: Workflow Execution[/bold yellow]",
        title="Two Neurons Demo"
    ))

    manager = WorkflowManager()

    # Create security audit workflow
    workflow = manager.create_workflow("security_audit")
    workflow.chain_steps.append({
        "neuron": "primary",
        "task": "vulnerability_scan"
    })
    workflow.chain_steps.append({
        "neuron": "secondary",
        "task": "compliance_check"
    })
    workflow.chain_steps.append({
        "neuron": "primary",
        "task": "patch_critical_vulnerabilities"
    })
    workflow.chain_steps.append({
        "neuron": "secondary",
        "task": "generate_audit_report"
    })

    console.print(f"\n[yellow]Workflow: {list(manager.list_workflows())[0]}[/yellow]")
    console.print(f"[dim]{len(workflow.chain_steps)} steps[/dim]\n")

    results = manager.execute_workflow("security_audit")

    console.print("\n[bold green]Audit Results:[/bold green]")
    for result in results:
        console.print(f"  ✓ {result['task']}: {result['status']}")


async def example_4_custom_neuron():
    """Example 4: Custom neuron with specialized tasks"""
    console.print(Panel(
        "[bold blue]Example 4: Custom Neuron[/bold blue]",
        title="Two Neurons Demo"
    ))

    executor = TaskExecutor()

    # Add custom neurons
    executor.add_custom_neuron("backup_manager")
    executor.add_custom_neuron("db_admin")

    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
    ) as progress:
        task1 = progress.add_task("Creating backup...", total=None)
        result1 = await executor.execute_task("backup_database", "backup_manager")
        progress.update(task1, description="✓ Backup created")

    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
    ) as progress:
        task2 = progress.add_task("Restoring database...", total=None)
        result2 = await executor.execute_task("restore_database", "db_admin")
        progress.update(task2, description="✓ Database restored")

    console.print(f"\n[blue]✓ Backup manager: {result1['task']}[/blue]")
    console.print(f"[blue]✓ DB admin: {result2['task']}[/blue]")


async def example_5_status_monitoring():
    """Example 5: Comprehensive status monitoring"""
    console.print(Panel(
        "[bold green]Example 5: Status Monitoring[/bold green]",
        title="Two Neurons Demo"
    ))

    executor = TaskExecutor()
    executor.add_custom_neuron("monitor")
    executor.add_custom_neuron("analytics")

    status = executor.get_all_status()

    table = Table(title="Neuron Status Overview")
    table.add_column("Neuron", style="cyan", justify="center")
    table.add_column("Type", style="yellow", justify="center")
    table.add_column("Status", style="green", justify="center")
    table.add_column("Uptime", style="blue", justify="center")

    for name, info in status.items():
        status_badge = "🟢" if info['status'] == 'active' else "🟡"
        table.add_row(
            name,
            info['type'].upper(),
            f"{status_badge} {info['status']}",
            f"{info['uptime']}s"
        )

    console.print(table)


async def example_6_complex_workflow():
    """Example 6: Complex multi-step workflow"""
    console.print(Panel(
        "[bold red]Example 6: Complex Workflow[/bold red]",
        title="Two Neurons Demo"
    ))

    manager = WorkflowManager()
    executor = manager.executor

    # Create deployment workflow
    workflow = manager.create_workflow("k8s_deployment")
    workflow.chain_steps.append({"neuron": "primary", "task": "build_image"})
    workflow.chain_steps.append({"neuron": "secondary", "task": "run_tests"})
    workflow.chain_steps.append({"neuron": "primary", "task": "deploy_to_cluster"})
    workflow.chain_steps.append({"neuron": "secondary", "task": "monitor_metrics"})
    workflow.chain_steps.append({"neuron": "primary", "task": "cleanup_resources"})
    workflow.chain_steps.append({"neuron": "secondary", "task": "verify_deployment"})

    console.print(f"\n[red]Workflow: {list(manager.list_workflows())[0]}[/red]")
    console.print(f"[dim]{len(workflow.chain_steps)} steps[/dim]\n")

    console.print("[bold]Executing deployment workflow...[/bold]")

    results = manager.execute_workflow("k8s_deployment")

    console.print("\n[bold green]Deployment Summary:[/bold green]")
    success_count = 0
    for result in results:
        if result['status'] == 'completed':
            success_count += 1
            console.print(f"  ✓ {result['task']}")
        else:
            console.print(f"  ✗ {result['task']}: {result['status']}")

    console.print(f"\n[dim]{success_count}/{len(results)} tasks completed successfully[/dim]")


async def example_7_real_world_simulation():
    """Example 7: Real-world DevOps scenario simulation"""
    console.print(Panel(
        "[bold orange]Example 7: Real-World Simulation[/bold orange]",
        title="Two Neurons Demo"
    ))

    # Setup: Add specialized custom neurons
    executor = TaskExecutor()
    executor.add_custom_neuron("secrets_manager")
    executor.add_custom_neuron("firewall_manager")
    executor.add_custom_neuron("log_aggregator")

    # Simulate incident response workflow
    console.print("\n[yellow]Simulating incident response...[/yellow]")

    tasks = [
        ("identify_threat", "secrets_manager"),
        ("block_ip", "firewall_manager"),
        ("collect_logs", "log_aggregator"),
        ("analyze_impact", "primary"),
        ("generate_report", "secondary"),
    ]

    for task, neuron in tasks:
        with Progress(
            SpinnerColumn(),
            "[progress.description]{task.description}",
        ) as progress:
            task_progress = progress.add_task(f"Processing {task}...", total=None)
            result = await executor.execute_task(task, neuron)
            progress.update(task_progress, description=f"✓ {task}")

    console.print(f"\n[orange]✓ Incident response completed in {len(tasks)} steps[/orange]")


async def main():
    """Run all examples with nice formatting"""
    rprint("[bold]╔════════════════════════════════════════════════════════════╗[/bold]")
    rprint("[bold]║         Two Neurons - DevOps CLI Examples                ║[/bold]")
    rprint("[bold]╚════════════════════════════════════════════════════════════╝[/bold]")

    await example_1_basic_execution()
    await asyncio.sleep(1)

    await example_2_chaining()
    await asyncio.sleep(1)

    await example_3_workflow()
    await asyncio.sleep(1)

    await example_4_custom_neuron()
    await asyncio.sleep(1)

    await example_5_status_monitoring()
    await asyncio.sleep(1)

    await example_6_complex_workflow()
    await asyncio.sleep(1)

    await example_7_real_world_simulation()

    console.print(Panel(
        "[bold green]╔════════════════════════════════════════════════════════════╗[/bold green]\n"
        "[bold green]║         All Examples Completed Successfully!              ║[/bold green]\n"
        "[bold green]║  Two Neurons is ready for production DevOps workflows!   ║[/bold green]\n"
        "[bold green]╚════════════════════════════════════════════════════════════╝[/bold green]",
        title="Demo Complete"
    ))


if __name__ == "__main__":
    asyncio.run(main())
