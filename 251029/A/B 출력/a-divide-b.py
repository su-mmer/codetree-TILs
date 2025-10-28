a, b = map(int, input().split())

total = str(a // b) + '.'
tmp = a % b

for _ in range(20):
    tmp *= 10
    total += str(tmp // b)
    tmp -= (tmp // b) * b

print(total)