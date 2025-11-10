def print_re(n):
    if n == 0:
        return

    print(n, end=' ')
    print_re(n-1)
    print(n, end=' ')


n = int(input())
print_re(n)