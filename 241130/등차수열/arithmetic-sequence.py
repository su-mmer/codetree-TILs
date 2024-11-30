n = int(input())
arr = list(map(int, input().split()))

max_count = 0
for i in range(min(arr) + 1, max(arr)):
    count = 0
    for j in range(len(arr)):  # ai
        for k in range(j + 1, len(arr)):  # aj
            if abs(arr[j] - i) == abs(arr[k] - i):
                count += 1

    max_count = max(count, max_count)

print(max_count)