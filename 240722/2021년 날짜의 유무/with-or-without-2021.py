m, d = map(int, input().split())

def is_date(m, d):
    if m == 2:
        if 1 <= d and d <= 28:
            return True
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= d and d <= 31:
            return True
    elif m in [4, 6, 9, 11]:
        if 1 <= d and d <= 30:
            return True


print ("Yes") if is_date(m, d) else print("No")