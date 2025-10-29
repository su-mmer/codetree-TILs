sum_val, cnt = 0, 0
while True:
    n = int(input())
    if 20 <= n and n <= 29:
        sum_val += n
        cnt += 1
    else:
        break

print(f"{sum_val/cnt:.2f}")