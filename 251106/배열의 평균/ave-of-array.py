arr = [ list(map(int, input().split())) for _ in range(2) ]

total_sum = 0
for i in range(2):
    sum_val = 0
    for j in range(4):
        sum_val += arr[i][j]
        total_sum += arr[i][j]
    print(f"{sum_val / 4:.1f}", end=' ')

print()

for i in range(4):
    sum_val = 0
    for j in range(2):
        sum_val += arr[j][i]
    print(f"{sum_val / 2:.1f}", end=' ')

print()
print(f"{total_sum / 8:.1f}")