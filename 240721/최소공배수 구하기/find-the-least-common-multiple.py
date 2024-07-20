n, m = map(int, input().split())

def calculate(n, m):
    gcd_value = 1
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd_value = i
    
    i = 1
    while True:
        value = gcd_value * i
        if value % n == 0 and value % m == 0:
            print(value)
            break
        i += 1

calculate(n, m)