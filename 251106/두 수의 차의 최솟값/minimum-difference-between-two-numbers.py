n = int(input())
arr = list(map(int, input().split()))

diff = 101
for i in range(n-1):
    for j in range(i+1, n):
        if arr[j] - arr[i] < diff:
            diff = arr[j] - arr[i]

print(diff)