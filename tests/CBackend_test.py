import time

import torch
from torch import nn
from python.backends.CBackend import CBackend

class OperatorModel(nn.Module):
    def __init__(self):
        super(OperatorModel, self).__init__()

    def forward(self, x: torch.Tensor, y: torch.Tensor):
        print("Forward pass")
        print(torch.add(x, y))
        print(torch.mul(x, y))
        print(torch.sub(x, y))
        print(torch.div(x, y))
        print(torch.relu(x))
        return torch.matmul(x, y)

model = OperatorModel()
a = torch.randn(2, 2)
b = torch.randn(2, 2)
torch_output = model(a, b)
print(a)
print(b)
print(torch_output)
backend_instance = CBackend()
compiled_model = torch.compile(model, backend=backend_instance)
compiled_output = compiled_model(a, b)
print(compiled_output)