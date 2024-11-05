x, y = tuple(map(int, input().split()))

max_val = 0
for num in range(x, y+1):
    num = str(num)
    sum_val = 0
    for n in num:
        sum_val += int(n)
    max_val = max(max_val, sum_val)

print(max_val)