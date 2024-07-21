a, op, b = input().split()

def calculate(a, op, b):
    a, b = int(a), int(b)
    if op == "+":
        print(f'{a} {op} {b} = ', end='')
        return a + b
    elif op == "-":
        print(f'{a} {op} {b} = ', end='')
        return a - b 
    elif op == "*":
        print(f'{a} {op} {b} = ', end='')
        return a * b
    elif op == "/":
        print(f'{a} {op} {b} = ', end='')
        return a / b
    else:
        return False

print(calculate(a, op, b))