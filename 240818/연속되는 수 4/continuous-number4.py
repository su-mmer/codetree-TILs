n = int(input())
arr = [int(input()) for _ in range(n)]

max_count, count = 0, 0
for i in range(n):
    if i >= 1 and arr[i-1] < arr[i]:
        count += 1
    else:
        count = 1

    max_count = max(max_count, count)

print(max_count)