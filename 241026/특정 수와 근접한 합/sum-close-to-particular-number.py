import sys
min_with_s = sys.maxsize

n, s = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = sum(arr)

for i in range(n):
    for j in range(1, n):
        min_with_s = min(min_with_s, abs(sum_arr - arr[i] - arr[j] - s))

print(min_with_s)