n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_count, count = 0, 0
for i in range(n):
    if i >= 1 and t < arr[i] and t < arr[i-1]:
        # print(arr[i-1], arr[i])
        count += 1
    else:
        count = 1

    max_count = max(max_count, count)

print(max_count)