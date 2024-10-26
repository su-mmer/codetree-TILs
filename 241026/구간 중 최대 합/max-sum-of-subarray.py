n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0
for i in range(n-k+1):
    sum_mini = 0
    for j in range(k):
        sum_mini += arr[i+j]
    max_sum = max(max_sum, sum_mini)
print(max_sum)