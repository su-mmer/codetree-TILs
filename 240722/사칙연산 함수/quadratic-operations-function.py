a, op, b = input().split()
a, b = int(a), int(b)

def plus(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return int(a / b)


if op == "+":
    print(f'{a} {op} {b} =', plus(a, b))
elif op == "-":
    print(f'{a} {op} {b} =', sub(a, b))
elif op == "*":
    print(f'{a} {op} {b} =', mul(a, b))
elif op == "/":
    print(f'{a} {op} {b} =', div(a, b))
else:
    print ("False")