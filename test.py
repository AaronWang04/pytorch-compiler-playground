import torch
from torch import nn
import custom_backend

class TestModel(nn.Module):
    def __init__(self, operation: str):
        super(TestModel, self).__init__()
        if operation not in ['add', 'mul']:
            raise ValueError("Supported operations are 'add' and 'mul'.")
        self.operation = operation

    def forward(self, inputs):
        for i in inputs: print(i)
        a, b = inputs
        if self.operation == 'add':
            return torch.add(a, b)
        elif self.operation == 'mul':
            return torch.mul(a, b)

model = TestModel('add')
a = torch.randn(2, 2)
b = torch.randn(2, 2)
compiled_model = torch.compile(model, backend=custom_backend.simple_pointwise_backend)
output = compiled_model((a, b))
print("Output:", output)
