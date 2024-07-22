a, b = map(int, input().split())

def calculate(m, n):
    if m < n:
        m += 10
        n *= 2
    else:
        m *= 2
        n += 10
    return m, n


a, b = calculate(a, b)
print(a, b)