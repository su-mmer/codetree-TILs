n = int(input())
arr = [ n * x for x in range(1, 11) ]

cnt = 0
for elem in arr:
    if cnt == 2:
        break
    if elem % 5 == 0:
        cnt += 1
    print(elem, end=' ')