n = int(input())

# n이 짝수면 2로 나누고 홀수면 3을 곱하고 1 더하기
# f(n) = f(n // 2) + 1
# 종료 조건: n == 1: return 1
def calculate(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return calculate(n // 2) + 1
    else:
        return calculate(n * 3 + 1) + 1


print(calculate(n))