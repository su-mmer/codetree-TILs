def make_num (n, m):
    i = 1
    while True:
        if (m * i) % n == 0:
            print(m * i)
            break
        i += 1


n, m = map(int, input().split())
make_num(n, m)