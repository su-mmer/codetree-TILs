a, b = map(int, input().split())

def calculate(m, n):
    if m < n:
        m *= 2
        n += 25
    else:
        n *= 2
        m += 25
    return m, n

a, b = calculate(a, b)
print(a, b)