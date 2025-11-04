arr = list(map(int, input().split()))

min_val, max_val = arr[0], arr[0]
for elem in arr[:-1]:
    if elem < min_val:
        min_val = elem
    if max_val < elem:
        max_val = elem

print(max_val, min_val, sep=' ')