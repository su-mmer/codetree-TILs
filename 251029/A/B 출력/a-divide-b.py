a, b = map(int, input().split())

total = str(a // b) + '.'
tmp = a % b * 10
for _ in range(20):
    total += str(tmp // b)
    tmp -= (tmp // b) * b * 10
    # tmp = (a % b) * 10 // b
    # total += str(tmp)

print(total)