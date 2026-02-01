def is_mynumber(n):
    if n % 2 == 0 and (n // 10 + n % 10) % 5 == 0:
        return True
    else:
        return False

n = int(input())
print("Yes") if is_mynumber(n) else print("No")