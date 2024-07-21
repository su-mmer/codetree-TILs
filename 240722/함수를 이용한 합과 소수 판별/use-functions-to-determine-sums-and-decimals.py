a, b = map(int, input().split())

def is_prime(n):
    # 1은 소수가 아니므로 n=1이면 return False하여 끝냄
    if n == 1:
        return False
    # 소수 판별 -> 소수가 아니면 return False
    for i in range(2, n):
        if n % i == 0:
            return False
    # 소수 판별 -> 소수이면 return True
    return True


def total_even(n):
    total = 0
    while n >= 1:
        total += n % 10
        n = n // 10

    return True if total % 2 == 0 else False


cnt = 0
for n in range(a, b + 1):
    if is_prime(n) and total_even(n):
        cnt += 1

print(cnt)