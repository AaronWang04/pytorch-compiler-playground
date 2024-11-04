import COperators

import math
import torch
from typing import Any, Callable

class CBackend:
    """
    Backend that uses torch's C++ implementation via pybind
    There should not be a bigdifference in performance between this and the torch eager
    Other than the compilation overhead
    """
    def __init__(self) -> None:
        pass
    
    def __call__(self, gm: torch.fx.GraphModule, example_inputs: Any) -> Callable:

        for node in gm.graph.nodes:
            if node.op == 'call_function':
                if node.target == torch.add:
                    node.target = COperators.tensor_add
                elif node.target == torch.mul:
                    node.target = COperators.tensor_mul
                elif node.target == torch.sub:
                    node.target = COperators.tensor_sub
                elif node.target == torch.div:
                    node.target = COperators.tensor_div
                elif node.target == torch.matmul:
                    node.target = COperators.tensor_matmul
        
        gm.recompile()

        return gm
    