import sys

n = int(input())
arr = list(map(int, input().split()))

INT_SIZE = sys.maxsize

min_sum = INT_SIZE

for i in range(n):
    dist = 0
    for j in range(n):
        dist += arr[j] * abs(i-j)

    min_sum = min(min_sum, dist)

print(min_sum)