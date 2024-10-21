import COperators

import torch

addition = COperators.double_add(3.5, 4)
assert addition == 7.5
subtraction = COperators.double_sub(4, 3)
assert subtraction == 1
product = COperators.double_mul(3, 4)
assert product == 12
division = COperators.double_div(4, 2)
assert division == 2

x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
result = COperators.tensor_add(x, y)
assert torch.equal(result, torch.tensor([[6, 8], [10, 12]]))
result = COperators.tensor_sub(x, y)
assert torch.equal(result, torch.tensor([[-4, -4], [-4, -4]]))
result = COperators.tensor_mul(x, y)
assert torch.equal(result, torch.tensor([[5, 12], [21, 32]]))
result = COperators.tensor_div(x, y)
assert torch.equal(result, torch.tensor([[1/5, 2/6], [3/7, 4/8]]))

print("All operations are correct")
