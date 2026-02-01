def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def multi (a, b):
    return a * b
def divide (a, b):
    return a // b

a, o, b = input().split()
a, b = int(a), int(b)

if o == "+":
    print(a, o, b, "=", plus(a, b))
elif o == "-":
    print(a, o, b, "=", minus(a, b))
elif o == "*":
    print(a, o, b, "=", multi(a, b))
elif o == "/":
    print(a, o, b, "=", divide(a, b))
else:
    print("False")