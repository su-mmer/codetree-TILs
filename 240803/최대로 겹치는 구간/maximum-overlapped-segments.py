n = int(input())
arr = [0 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b):
        arr[i] += 1

print(max(arr))