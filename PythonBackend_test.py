import torch
from torch import nn
from PythonBackend import PythonBackend

"""
Demonstrates the torch computation graph and how it can be modified
"""

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()

    def forward(self, x, y):
        return torch.mul(x, y)
    
model = Model()
a = torch.randn(2, 2)
b = torch.randn(2, 2)
backend_instance = PythonBackend()
compiled_model = torch.compile(model, backend=backend_instance)
output = compiled_model(a, b)

print(a)
print(b)
print(output)
