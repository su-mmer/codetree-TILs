a = input()
b = input()

while b in a:
    pv = a.index(b)
    a = a[:pv] + a[pv+len(b):]

print(a)