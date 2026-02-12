"""Simple example usage of Two Neurons CLI"""

import asyncio
from two_neurons import PrimaryNeuron, SecondaryNeuron, TaskExecutor, TaskChain, WorkflowManager


async def example_basic_tasks():
    """Example 1: Basic task execution"""
    print("\n[bold cyan]=== Example 1: Basic Tasks ===[/bold cyan]")

    executor = TaskExecutor()

    # Execute task on primary neuron
    result1 = await executor.execute_task("deploy_service", "primary")
    print(f"Primary Result: {result1}")

    # Execute task on secondary neuron
    result2 = await executor.execute_task("health_check", "secondary")
    print(f"Secondary Result: {result2}")


async def example_chaining():
    """Example 2: Chain operations"""
    print("\n[bold cyan]=== Example 2: Chain Operations ===[/bold cyan]")

    executor = TaskExecutor()

    # Chain: Primary → Secondary
    chain = TaskChain(executor)
    chain.add_step("primary", "analyze_logs")
    chain.add_step("secondary", "generate_report")

    results = await chain.execute_chain()
    print(f"Chain Results: {results}")


async def example_workflow():
    """Example 3: Workflow execution"""
    print("\n[bold cyan]=== Example 3: Workflow Execution ===[/bold cyan]")

    manager = WorkflowManager()

    # Create a security audit workflow
    workflow = manager.create_workflow("security_audit")
    workflow.chain_steps.append({"neuron": "primary", "task": "scan_vulnerabilities"})
    workflow.chain_steps.append({"neuron": "secondary", "task": "report_findings"})
    workflow.chain_steps.append({"neuron": "primary", "task": "patch_vulnerabilities"})

    print(f"Workflow steps: {manager.get_workflow('security_audit').get_chain_info()}")

    # Execute the workflow
    results = manager.execute_workflow("security_audit")
    print(f"Workflow Results: {results}")


async def example_custom_neuron():
    """Example 4: Custom Neuron"""
    print("\n[bold cyan]=== Example 4: Custom Neuron ===[/bold cyan]")

    executor = TaskExecutor()
    executor.add_custom_neuron("custom_ops")

    result = await executor.execute_task("custom_task", "custom_ops")
    print(f"Custom Neuron Result: {result}")


async def example_status():
    """Example 5: Get Status"""
    print("\n[bold cyan]=== Example 5: Get Status ===[/bold cyan]")

    executor = TaskExecutor()
    executor.add_custom_neuron("monitor")

    status = executor.get_all_status()
    for neuron_name, neuron_status in status.items():
        print(f"{neuron_name}: {neuron_status}")


async def main():
    """Run all examples"""
    await example_basic_tasks()
    await example_chaining()
    await example_workflow()
    await example_custom_neuron()
    await example_status()

    print("\n[bold green]=== All Examples Completed ===[/bold green]")


if __name__ == "__main__":
    asyncio.run(main())
