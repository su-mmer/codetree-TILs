n = int(input())

# f(n) = (f(n-1)*f(n-2)) % 100
# 종료 조건: f(1) == 2, f(2) == 4
def calculate(n):
    if n == 1:
        return 2
    if n == 2:
        return 4

    return (calculate(n - 1) * calculate(n - 2)) % 100


print(calculate(n))