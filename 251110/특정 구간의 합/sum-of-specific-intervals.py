n, m = map(int, input().split())
arr = list(map(int, input().split()))


def calculate(a, b):
    sum_val = 0
    for i in arr[a-1:b]:
        sum_val += i
    return sum_val


for i in range(m):
    a, b = map(int, input().split())
    print(calculate(a, b))