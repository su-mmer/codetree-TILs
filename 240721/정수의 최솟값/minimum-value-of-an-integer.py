a, b, c = map(int, input().split())

def minimul(a, b,c ):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= a and c <= b:
        return c


print(minimul(a, b, c))