# Two Neurons - Usage Examples

This directory contains examples of how to use the Two Neurons CLI tool.

## Example Files

### `usage_examples.py`

A simple example showing basic features:

```bash
python examples/usage_examples.py
```

### `robust_example.py`

A comprehensive, robust example showcasing all features with beautiful formatting:

```bash
python examples/robust_example.py
```

## What You'll See

### Basic Examples (`usage_examples.py`)

1. **Basic Tasks**
   - Running tasks on primary and secondary neurons
   - Simple task processing

2. **Chain Operations**
   - Chaining tasks between neurons
   - Sequential execution patterns

3. **Workflow Management**
   - Creating workflows with multiple steps
   - Executing complete workflows

4. **Custom Neurons**
   - Adding custom neuron types
   - User-defined task processing

5. **Status Monitoring**
   - Checking neuron status
   - Viewing uptime and activity

### Robust Examples (`robust_example.py`)

1. **Basic Execution**
   - Deployments and health checks with progress indicators

2. **Task Chaining**
   - Multi-step chains with detailed results

3. **Workflow Execution**
   - Complete security audit workflow with audit reports

4. **Custom Neuron**
   - Specialized custom neurons for backup and database operations

5. **Status Monitoring**
   - Comprehensive table view of all neuron statuses

6. **Complex Workflow**
   - Large Kubernetes deployment workflow with multiple steps

7. **Real-World Simulation**
   - Incident response workflow simulating real DevOps scenarios

## Running the Examples

```bash
# Make sure the package is installed
pip install https://github.com/hallucinaut/two-neurons

# Run the simple examples
python examples/usage_examples.py

# Run the robust examples
python examples/robust_example.py
```

## Expected Output

Each example will output the results of the neuron operations, showing the task, status, and neuron information. The robust examples use the `rich` library for beautiful terminal output with colors, progress bars, and formatted tables.

## Customization

You can modify the examples to:

- Add your own tasks
- Create custom neuron types
- Design complex workflows
- Test different chaining strategies
- Simulate real DevOps scenarios
