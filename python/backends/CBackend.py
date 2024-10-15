import operator

import math
import torch
from typing import Any, Callable

class CBackend:
    """
    Backend that uses C++ implementation instead of Torch's BLAS implementation
    """
    def __init__(self) -> None:
        pass
