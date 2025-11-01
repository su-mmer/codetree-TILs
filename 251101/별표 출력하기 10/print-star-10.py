n = int(input())

cnt_even, cnt_odd = 1, n
for i in range(n):
    if i % 2 == 0:
        for j in range(cnt_even):
            print("*", end=' ')
        cnt_even += 1
    else:
        for j in range(cnt_odd):
            print("*", end=' ')
        cnt_odd -= 1
    print()

cnt_even -= 1
cnt_odd += 1
for i in range(n):
    if i % 2 == 0:
        for j in range(cnt_even):
            print("*", end=' ')
        cnt_even -= 1
    else:
        for j in range(cnt_odd):
            print("*", end=' ')
        cnt_odd += 1
    print()