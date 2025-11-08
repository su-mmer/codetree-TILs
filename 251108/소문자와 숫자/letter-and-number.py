string = input()

for char in string:
    if 'A' <= char and char <= 'Z':
        print(char.lower(), end='')
    elif 'a' <= char and char <= 'z':
        print(char, end='')
    elif char.isdigit():
        print(char, end='')