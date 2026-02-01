def is_yoon (n):
    if n % 100 == 0 and n % 400 != 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False

y = int(input())
print("true") if is_yoon(y) else print("false")