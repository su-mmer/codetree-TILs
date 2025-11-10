a = input()
b = input()

def is_part():
    if b in a:
        return a.index(b)
    else:
        return -1

print(is_part())