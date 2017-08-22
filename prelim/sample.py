
a = 10
b = 0

try:
    assert (a == 0), ArithmeticError
    print(a/b)

except ArithmeticError: print("Cannot divide by zero")