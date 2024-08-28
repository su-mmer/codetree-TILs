n = int(input())
arr = list(map(int, input().split()))

num = 0
for i in range(n):
    for j in range(i + 2, n):
        num = max(arr[i] + arr[j], num)

print(num)