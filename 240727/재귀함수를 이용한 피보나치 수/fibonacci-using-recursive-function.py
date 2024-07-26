n = int(input())

def calculate(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    return calculate(n - 1) + calculate(n - 2)


print(calculate(n))