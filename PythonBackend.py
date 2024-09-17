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

def matmul(a, b):
    return torch.matmul(a, b)

def exp(a):
    return torch.exp(a)

def log(a):
    return torch.log(a)

def sin(a):
    return torch.sin(a)

def cos(a):
    return torch.cos(a)

def power(a, b):
    return torch.pow(a, b)

class PythonBackend:
    """
    """
    def __init__(self):
        pass

    def __call__(self, gm: torch.fx.GraphModule, example_inputs: Any) -> Callable:
        
        print(gm.graph)
        
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
                elif node.target == torch.matmul:
                    node.target = matmul
                elif node.target == torch.exp:
                    node.target = exp
                elif node.target == torch.log:
                    node.target = log
                elif node.target == torch.sin:
                    node.target = sin
                elif node.target == torch.cos:
                    node.target = cos
                elif node.target == torch.pow:
                    node.target = power
                else:
                    raise NotImplementedError(f"Operation {node.target} not supported.")

        gm.recompile()

        print(gm.graph)
        
        return gm