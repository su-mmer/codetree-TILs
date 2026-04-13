import sys
arr = list(map(int, input().split()))
n = 6

def get_diff(i, j, k):
    sum1 = arr[i] + arr[j] + arr[k]
    sum2 = sum(arr) - sum1
    return abs(sum1 - sum2)


min_score = sys.maxsize 
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            min_score = min(min_score, get_diff(i, j, k))

print(min_score)