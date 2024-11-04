import torch
from torch import nn
from backends.ToyBackend import ToyBackend

"""
Demonstrates the torch computation graph and how it can be modified
"""

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()

    def forward(self, x):
        x = torch.mul(x, 2)
        x = torch.add(x, 1)
        x = torch.mul(x, 3)
        return x
    
model = Model()
a = torch.randn(2, 2)
backend_instance = ToyBackend()
compiled_model = torch.compile(model, backend=backend_instance)
output = compiled_model(a)

print(a)
print(output)
