n, k = map(int, input().split())
arr = [0 for _ in range(n + 1)]  # 1번부터 n번까지

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        arr[i] += 1

print(max(arr))