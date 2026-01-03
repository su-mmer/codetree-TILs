n, m = map(int, input().split())

def print_num(n, m):
    if m < n:
        swap(n, m)  # always n < m
    
    num = 0
    for i in range(1, n+1):
        for _ in range(1, m+1):
            if n % i == 0 and m % i == 0:
                num = i

    print(num)

print_num(n, m)