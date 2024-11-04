import time
import torch
from torch import nn
import argparse

from backends.ToyBackend import ToyBackend
from backends.PythonBackend import PythonBackend
from backends.CBackend import CBackend

class ToyModel(nn.Module):

    def __init__(self):
        super(ToyModel, self).__init__()

    def forward(self, x):
        x = torch.mul(x, 2)
        x = torch.add(x, 1)
        x = torch.mul(x, 3)
        return x

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

# Argument parser for CLI options
parser = argparse.ArgumentParser(description='Select model, backend, and whether to compare execution time.')
parser.add_argument('--model', choices=['toy', 'operator', 'matmul'], default='toy', help='Which model to use')
parser.add_argument('--backend', choices=['toy', 'python', 'c'], default='toy', help='Which backend to use')
parser.add_argument('--time', action='store_true', help='Compare execution time with regular execution')

args = parser.parse_args()

# Dictionaries to map string inputs to classes
model_dict = {
    'toy': ToyModel,
    'operator': OperatorModel,
    'matmul': MatmulModel,
}

backend_dict = {
    'toy': ToyBackend,
    'python': PythonBackend,
    'c': CBackend,
}

# Instantiate the selected model and backend
model_class = model_dict[args.model]
model = model_class()

backend_class = backend_dict[args.backend]
backend_instance = backend_class()

# Prepare inputs based on the selected model
if args.model == 'toy':
    x = torch.randn(100)
elif args.model == 'operator':
    x = torch.randn(100, 100)
    y = torch.randn(100, 100)
elif args.model == 'matmul':
    x = torch.randn(100, 100)
    y = torch.randn(100, 100)

if args.time:
    # Run and time the regular model
    start_time = time.time()
    if args.model == 'toy':
        torch_output = model(x)
    elif args.model == 'operator':
        torch_output = model(x, y)
    elif args.model == 'matmul':
        torch_output = model(x, y)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Regular PyTorch Output:")
    print(torch_output)
    print(f"PyTorch elapsed time: {elapsed_time:.6f} seconds")

# Compile the model with the selected backend
compiled_model = torch.compile(model, backend=backend_instance)

# Run and time the compiled model
start_time = time.time()
if args.model == 'toy':
    compiled_output = compiled_model(x)
elif args.model == 'operator':
    compiled_output = compiled_model(x, y)
elif args.model == 'matmul':
    compiled_output = compiled_model(x, y)
end_time = time.time()
elapsed_time_2 = end_time - start_time
print(f"\nCompiled Model Output with {args.backend.capitalize()}Backend:")
print(compiled_output)
print(f"{args.backend.capitalize()}Backend elapsed time: {elapsed_time_2:.6f} seconds")

if args.time:
    # Compare outputs and performance
    if torch.allclose(torch_output, compiled_output, atol=1e-4):
        print("Outputs are the same.")
    else:
        print("Outputs differ!")
    ratio = elapsed_time_2 / elapsed_time
    if ratio < 1:
        print(f"Speedup: {1/ratio:.2f}x faster")
    else:
        print(f"Slowdown: {ratio:.2f}x slower")
