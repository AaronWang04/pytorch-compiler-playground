import operators

addition = operators.add(3.5, 4)
assert addition == 7.5
subtraction = operators.subtract(4, 3)
assert subtraction == 1
product = operators.mul(3, 4)
assert product == 12
division = operators.div(4, 2)
assert division == 2

print("All operations are correct")
