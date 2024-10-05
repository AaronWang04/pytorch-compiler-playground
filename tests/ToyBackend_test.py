import torch
from torch import nn
from python.backends import ToyBackend

"""
Demonstrates the torch computation graph and how it can be modified
"""

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()

    def forward(self, x):
        return torch.mul(x, 2)
    
model = Model()
a = torch.randn(2, 2)
backend_instance = ToyBackend()
compiled_model = torch.compile(model, backend=backend_instance)
output = compiled_model(a)

print(a)
print(output)
