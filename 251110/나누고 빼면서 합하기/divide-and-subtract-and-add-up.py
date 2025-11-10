n, m = map(int, input().split())
arr = list(map(int, input().split()))

def calculate(m):
    sum_val = arr[m-1]
    while m != 1:
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
        sum_val += arr[m-1]
    return sum_val


print(calculate(m))