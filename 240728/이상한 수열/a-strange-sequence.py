n = int(input())

# f(n) = f(n // 3) + f(n - 1)
# 종료 조건: f(1) == 1, f(2) == 2
def calculate(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return calculate(n // 3) + calculate(n - 1)


print(calculate(n))