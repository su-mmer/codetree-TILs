n, m = map(int, input().split())

def calculate(n, m):
    small = n if n < m else m
    big = n if n > m else m
    value = 1
    for i in range(1, small+1):
        if big % i == 0 and small % i ==0:
            value = i
    
    print(value)

calculate(n, m)