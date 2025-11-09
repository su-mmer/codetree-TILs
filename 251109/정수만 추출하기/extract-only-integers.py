a, b = tuple(input().split())

a_int, b_int = '', ''
for c in a:
    if c.isdigit():
        a_int += c
    else:
        break

for c in b:
    if c.isdigit():
        b_int += c
    else:
        break

print(int(a_int) + int(b_int))