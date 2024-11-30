n = int(input())
arr = [ int(input()) for _ in range(n) ] + [0]

max_count = 0
for h in range(min(arr), max(arr) + 1):
    ice = 0
    for i in range(len(arr)):
        if (arr[i - 1] - h) > 0 and (arr[i] - h) <= 0:
            ice += 1
    max_count = max(max_count, ice)

print(max_count)