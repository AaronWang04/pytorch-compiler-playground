import math
import torch
from typing import Any, Callable

class PythonBackend:
    """
    Backend that uses python implementation instead of Torch's BLAS implementation
    Expect major slowdowns
    """
    def __init__(self):
        pass

    def __call__(self, gm: torch.fx.GraphModule, example_inputs: Any) -> Callable:
        
        # print(gm.graph)
        
        for node in gm.graph.nodes:
            if node.op == 'call_function':
                if node.target == torch.add:
                    node.target = PythonBackend.add
                elif node.target == torch.mul:
                    node.target = PythonBackend.mul
                elif node.target == torch.sub:
                    node.target = PythonBackend.sub
                elif node.target == torch.div:
                    node.target = PythonBackend.div
                elif node.target == torch.relu:
                    node.target = PythonBackend.relu
                elif node.target == torch.matmul:
                    node.target = PythonBackend.matmul
                elif node.target == torch.exp:
                    node.target = PythonBackend.exp
                elif node.target == torch.log:
                    node.target = PythonBackend.log
                elif node.target == torch.sin:
                    node.target = PythonBackend.sin
                elif node.target == torch.cos:
                    node.target = PythonBackend.cos
                elif node.target == torch.pow:
                    node.target = PythonBackend.power
                else:
                    raise NotImplementedError(f"Operation {node.target} not supported.")

        gm.recompile()

        # print(gm.graph)

        return gm
    
    # Define custom functions
    @staticmethod
    def add(a: torch.Tensor, b: torch.Tensor | torch.NumberType):
        return a + b

    @staticmethod
    def mul(a: torch.Tensor, b: torch.Tensor | torch.NumberType):
        return a * b

    @staticmethod
    def sub(a: torch.Tensor, b: torch.Tensor | torch.NumberType):
        return a - b

    @staticmethod
    def div(a: torch.Tensor, b: torch.Tensor | torch.NumberType):
        return a / b

    @staticmethod
    def relu(a: torch.Tensor):
        return a * (a > 0)

    def matmul(a: torch.Tensor, b: torch.Tensor):
        # Matrix multiplication of two 2D tensors
        m, n = a.shape
        n_t, p = b.shape
        assert n == n_t, "Tensor dimensions must match for matrix multiplication"
        c = torch.zeros(m, p)
        for i in range(m):
            for j in range(p):
                sum = 0
                for k in range(n):
                    sum += a[i, k] * b[k, j]
                c[i, j] = sum
        return c

    @staticmethod
    def exp(a: torch.Tensor):
        return torch.exp(a)

    @staticmethod
    def log(a: torch.Tensor):
        return torch.log(a)
    
    def sin(a: torch.Tensor):
        return torch.sin(a)

    def cos(a: torch.Tensor):
        return torch.cos(a)
    
    @staticmethod
    def power(a: torch.Tensor, b: torch.Tensor):
        return PythonBackend.exp(b * PythonBackend.log(a))