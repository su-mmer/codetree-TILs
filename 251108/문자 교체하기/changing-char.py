a, b = tuple(input().split())
b = list(b)

b[:2] = a[:2]
b = ''.join(b)
print(b)