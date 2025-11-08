a, b = tuple(input().split())

print (ord(a) + ord(b), end=' ')

print(ord(b) - ord(a)) if ord(a) < ord(b) else print(ord(a) - ord(b))
    