n = int(input())

def calculate(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return calculate(n // 2) + 1
    else:
        return calculate(n // 3) + 1


print(calculate(n))