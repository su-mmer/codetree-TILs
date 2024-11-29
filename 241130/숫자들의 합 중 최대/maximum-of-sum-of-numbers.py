x, y = tuple(map(int, input().split()))

max_num = 0
for i in range(x, y + 1):
    add_num = 0
    for j in (str(i)):
        add_num += int(j)
    max_num = max(max_num, add_num)

print(max_num)