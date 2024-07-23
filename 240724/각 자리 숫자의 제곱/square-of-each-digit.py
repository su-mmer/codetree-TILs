n = int(input())

def plus(n):
    if n == 0:
        return 0

    return plus(n // 10) + (n % 10) ** 2


print(plus(n))