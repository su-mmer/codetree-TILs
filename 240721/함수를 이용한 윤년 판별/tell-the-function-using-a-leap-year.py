y = int(input())

def is_leap(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

print("true") if is_leap(y) else print("false")