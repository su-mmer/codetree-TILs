def add(a, b, c):
    if a < b and a < c:
        return a
    elif b < c and b < a:
        return b
    else:
        return c


a, b, c = map(int, input().split())
print(add(a, b, c))