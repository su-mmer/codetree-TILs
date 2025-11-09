def make_num(n, m):
    min_num = n if n > m else m

    for i in range(min_num+1, 0, -1):
        if n % i == 0 and m % i == 0:
            print(i)
            break


n, m = map(int, input().split())
make_num(n, m)