n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
bucket = [0] * 401
for i in range(n):
    bucket[arr[i][1]] += arr[i][0]

max_val = 0
for i in range(1+k, 401-k):
    sum_val = 0
    for j in range(i-k, i+k+1):
        sum_val += bucket[j]
    max_val = max(max_val, sum_val)

print(max_val)