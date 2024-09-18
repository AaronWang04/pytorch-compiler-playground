import time

import torch
from torch import nn
from python.PythonBackend import PythonBackend

"""
Demonstrates the torch computation graph and how it can be modified
"""
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
    
class MatmulModel(nn.Module):
    def __init__(self):
        super(MatmulModel, self).__init__()
    
    def forward(self, x: torch.Tensor, y: torch.Tensor, n: int = 1):
        for i in range(n-1):
            torch.matmul(x, y)
        return torch.matmul(x, y)
    
# model = OperatorModel()
# a = torch.randn(2, 2)
# b = torch.randn(2, 2)
# torch_output = model(a, b)
# print(a)
# print(b)
# print(torch_output)
# backend_instance = PythonBackend()
# compiled_model = torch.compile(model, backend=backend_instance)
# compiled_output = compiled_model(a, b)
# print(compiled_output)

model = MatmulModel()
a = torch.randn(100, 100)
b = torch.randn(100, 100)
start_time = time.time()
torch_output = model(a, b)
end_time = time.time()
elapsed_time = end_time - start_time
print(torch_output)
print(f"PyTorch elapsed time: {elapsed_time:.6f} seconds")
backend_instance = PythonBackend()
compiled_model = torch.compile(model, backend=backend_instance)
start_time = time.time()
compiled_output = compiled_model(a, b)
end_time = time.time()
elapsed_time_2 = end_time - start_time
print(compiled_output)
print(f"PythonBackend elapsed time: {elapsed_time_2:.6f} seconds")
print(f"Slow down: {elapsed_time_2/elapsed_time*100:.3f}%")
