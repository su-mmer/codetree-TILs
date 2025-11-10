a = input()
b = input()

def is_part():
    if b in a:
        return a.index(b)
    else:
        return False

print(is_part()) if is_part() else print(-1)