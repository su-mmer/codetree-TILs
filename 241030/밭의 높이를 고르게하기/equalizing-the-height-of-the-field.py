import sys
num, height, time = map(int, input().split())
arr = list(map(int, input().split()))

min_price = sys.maxsize
for i in range(num - time + 1):
    price = 0
    for k in range(i, i + time):
        price += abs(arr[k] - height)
    min_price = min(min_price, price)

print(min_price)