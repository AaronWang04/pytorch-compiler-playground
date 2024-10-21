import COperators

addition = COperators.double_add(3.5, 4)
assert addition == 7.5
subtraction = COperators.double_sub(4, 3)
assert subtraction == 1
product = COperators.double_mul(3, 4)
assert product == 12
division = COperators.double_div(4, 2)
assert division == 2

print("All operations are correct")
