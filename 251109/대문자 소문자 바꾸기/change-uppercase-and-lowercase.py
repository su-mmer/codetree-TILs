string = input()

for c in string:
    if 'A' <= c and c <= 'Z':
        print(c.lower(), end='')
    elif 'a' <= c and c <= 'z':
        print(c.upper(), end='')