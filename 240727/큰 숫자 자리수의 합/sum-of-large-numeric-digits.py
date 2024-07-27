a, b, c = map(int, input().split())
# 세 숫자를 곱한 후 각 자리 숫자들의 합을 구하기
# f(n): f(n // 10) + n % 10
# 종료 조건: n < 10 -> return n
def calculate(n):
    if n < 10:
        return n
        
    return calculate(n // 10) + n % 10


print(calculate(a * b * c))