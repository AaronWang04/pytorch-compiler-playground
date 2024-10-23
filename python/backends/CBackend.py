import COperators

import math
import torch
from typing import Any, Callable

class CBackend:
    """
    Backend that uses torch's C++ implementation via pybind
    """
    def __init__(self) -> None:
        pass
    
    def __call__(self, gm: torch.fx.GraphModule, example_inputs: Any) -> Callable:

        print(gm.graph)

        for node in gm.graph.nodes:
            if node.op == 'call_function':
                if node.target == torch.add:
                    node.target = CBackend.tensor_add
                elif node.target == torch.mul:
                    node.target = CBackend.tensor_mul
                elif node.target == torch.sub:
                    node.target = CBackend.tensor_sub
                elif node.target == torch.div:
                    node.target = CBackend.tensor_div
                elif node.target == torch.matmul:
                    node.target = CBackend.tensor_matmul
        
        gm.recompile()
        
        print()
        print(gm.graph)