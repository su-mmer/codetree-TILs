string = input()
part = input()

def is_part():
    if part in string:
        return True
    else:
        return False

if is_part():
    print(string.index(part))
else:
    print(-1)