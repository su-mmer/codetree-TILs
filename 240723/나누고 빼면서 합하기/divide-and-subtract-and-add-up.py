n, m = map(int, input().split())
arr = list(map(int, input().split()))

def calculate(m):
    total = 0
    while m >= 1:
        total += arr[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return total


print(calculate(m))