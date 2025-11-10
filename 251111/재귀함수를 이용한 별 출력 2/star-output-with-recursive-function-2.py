def print_start(n):
    if n == 0:
        return
    
    print("* " * n)
    print_start(n-1)
    print("* " * n)


n = int(input())
print_start(n)