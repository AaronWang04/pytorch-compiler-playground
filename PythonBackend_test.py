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
        print("Forward pass")
        print(torch.add(x, y))
        print(torch.mul(x, y))
        print(torch.sub(x, y))
        print(torch.div(x, y))
        print(torch.relu(x))
        return torch.matmul(x, y)
    
model = Model()
a = torch.randn(2, 2)
b = torch.randn(2, 2)
torch_output = model(a, b)
print(a)
print(b)
print(torch_output)
backend_instance = PythonBackend()
compiled_model = torch.compile(model, backend=backend_instance)
compiled_output = compiled_model(a, b)
print(compiled_output)
