import operator

if __name__ == "__main__":
    addition = operator.add(3, 4)
    assert addition == 7
    product = operator.mul(3, 4)
    assert product == 12
    print("Addition and product are correct")
