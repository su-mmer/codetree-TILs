n = int(input())

def plus(n):
    if n == 1:
        return 1
    
    return plus(n - 1) + n


print(plus(n))