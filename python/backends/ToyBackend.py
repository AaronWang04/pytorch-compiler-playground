import torch
from typing import Any, Callable

class ToyBackend:
    """
    Sample backend that replaces multiply with adding, not very useful but demonstrates
    how torch dynamo
    """
    def __init__(self) -> None:
        pass

    def __call__(self, gm: torch.fx.GraphModule, example_inputs: Any) -> Callable:
        """
        This method is called by torch.compile to compile the graph_module.
        """
        
        print(gm.graph)

        for node in gm.graph.nodes:
            if node.op == 'call_function':
                if node.target == torch.mul:
                    node.target = torch.add

        gm.recompile()

        print(gm.graph)

        return gm
