a, b = map(int, input().split())
satisfied = False

for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        satisfied = True

print(1) if satisfied else print(0)