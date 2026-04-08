n, k = map(int, input().split())
numbers = list(map(int, input().split()))

max_val = 0
for i in range(n - k + 1):
    val = 0
    for j in range(i, i+k):
        val += numbers[j]
    max_val = max(val, max_val)

print(max_val)