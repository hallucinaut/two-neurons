"""Chain operations between neurons"""

from typing import List, Dict, Any
from .neuron import Neuron
from .executor import TaskExecutor


class TaskChain:
    """Chain of tasks between neurons"""

    def __init__(self, executor: TaskExecutor):
        self.executor = executor
        self.chain_steps: List[Dict[str, Any]] = []

    def add_step(self, neuron_name: str, task: str) -> None:
        """Add a step to the chain"""
        self.chain_steps.append({
            "neuron": neuron_name,
            "task": task
        })

    async def execute_chain(self) -> List[Dict[str, Any]]:
        """Execute the entire chain"""
        results = []
        for step in self.chain_steps:
            neuron = self.executor.get_neuron(step["neuron"])
            if neuron:
                result = await neuron.process(step["task"])
                results.append(result)
        return results

    def get_chain_info(self) -> List[Dict[str, str]]:
        """Get information about the chain"""
        return [
            {"step": i + 1, "neuron": step["neuron"], "task": step["task"]}
            for i, step in enumerate(self.chain_steps)
        ]


class WorkflowManager:
    """Manage multiple workflows"""

    def __init__(self):
        self.workflows: Dict[str, TaskChain] = {}
        self.executor = TaskExecutor()

    def create_workflow(self, name: str) -> TaskChain:
        """Create a new workflow"""
        if name not in self.workflows:
            self.workflows[name] = TaskChain(self.executor)
        return self.workflows[name]

    def get_workflow(self, name: str) -> TaskChain:
        """Get an existing workflow"""
        return self.workflows.get(name)

    def execute_workflow(self, name: str) -> List[Dict[str, Any]]:
        """Execute a workflow"""
        if name not in self.workflows:
            return []
        chain = self.workflows[name]
        return asyncio.run(chain.execute_chain())

    def list_workflows(self) -> List[str]:
        """List all workflow names"""
        return list(self.workflows.keys())
