"""Task executor for Two Neurons"""

from typing import List, Dict, Any
from .neuron import Neuron, PrimaryNeuron, SecondaryNeuron, CustomNeuron, NeuronType


class TaskExecutor:
    """Executor for neuron tasks"""

    def __init__(self):
        self.primary = PrimaryNeuron()
        self.secondary = SecondaryNeuron()
        self.custom_neurons: Dict[str, CustomNeuron] = {}

    def add_custom_neuron(self, name: str) -> None:
        """Add a custom neuron"""
        if name not in self.custom_neurons:
            self.custom_neurons[name] = CustomNeuron(name)

    def get_neuron(self, name: str) -> Optional[Neuron]:
        """Get a neuron by name"""
        if name == "primary":
            return self.primary
        elif name == "secondary":
            return self.secondary
        return self.custom_neurons.get(name)

    async def execute_task(self, task: str, neuron_name: str) -> Dict[str, Any]:
        """Execute a task on a neuron"""
        neuron = self.get_neuron(neuron_name)
        if not neuron:
            return {"error": f"Neuron '{neuron_name}' not found"}
        return await neuron.process(task)

    async def chain_tasks(self, tasks: List[str], chain_type: str) -> List[Dict[str, Any]]:
        """Chain tasks between neurons"""
        results = []
        if chain_type == "primary_to_secondary":
            for task in tasks:
                primary_result = await self.primary.process(task)
                results.append(primary_result)
                secondary_result = await self.secondary.process(f"validate_{task}")
                results.append(secondary_result)
        elif chain_type == "secondary_to_primary":
            for task in tasks:
                secondary_result = await self.secondary.process(task)
                results.append(secondary_result)
                primary_result = await self.primary.process(f"execute_{task}")
                results.append(primary_result)
        return results

    def get_all_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all neurons"""
        return {
            "primary": self.primary.get_status(),
            "secondary": self.secondary.get_status(),
            **{name: neuron.get_status() for name, neuron in self.custom_neurons.items()}
        }
