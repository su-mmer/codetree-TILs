arr = list(map(int, input().split()))

max_val, min_val = -1, 1001
for elem in arr:
    if elem < 500 and max_val < elem:
        max_val = elem
    elif elem > 500 and elem < min_val:
        min_val = elem;

print(max_val, min_val, sep=' ')