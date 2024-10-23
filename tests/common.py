import torch
from torch import nn

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