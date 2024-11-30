x, y = tuple(map(int, input().split()))

count = 0
for i in range(x, y + 1):
    number = str(i)
    for n in range(len(number) // 2):
        if number[n] != number[-(n + 1)]:
            continue
        count += 1

print(count)