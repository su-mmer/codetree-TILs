arr = list(map(int, input().split()))

sum_val, count = 0, 0
for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        sum_val += i
        count += 1

print(f"{count} {sum_val}")