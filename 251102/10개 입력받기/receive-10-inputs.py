arr = list(map(int, input().split()))

sum_val, count = 0, 0
for i in arr:
    if i == 0:
        break
    sum_val += i
    count += 1

print(f"{sum_val} {sum_val/count:.1f}")