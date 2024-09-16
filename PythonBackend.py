import torch
from typing import Any, Callable

# Define custom functions
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def relu(a):
    return torch.relu(a)

class PythonBackend:
    """
    """
    def __init__(self):
        pass

    def __call__(self, gm: torch.fx.GraphModule, example_inputs: Any) -> Callable:
        
        print(gm.graph)
        
        operations = set()
        for node in gm.graph.nodes:
            if node.op == 'call_function':
                if node.target == torch.add:
                    node.target = add
                elif node.target == torch.mul:
                    node.target = mul
                elif node.target == torch.sub:
                    node.target = sub
                elif node.target == torch.div:
                    node.target = div
                elif node.target == torch.relu:
                    node.target = relu
                else:
                    raise NotImplementedError(f"Operation {node.target} not supported.")
        
        gm.recompile()

        print(gm.graph)
        return gm