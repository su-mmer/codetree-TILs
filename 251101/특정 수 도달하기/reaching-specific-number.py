arr = list(map(int, input().split()))

sum_val, cnt = 0, 0
for elem in arr:
    if elem >= 250:
        break
        
    sum_val += elem
    cnt += 1

print(f"{sum_val} {sum_val / cnt:.1f}")