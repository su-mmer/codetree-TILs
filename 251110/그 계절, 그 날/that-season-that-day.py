def is_leap(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    return False

def is_right_date(y, m, d):
    if is_leap(y) and m == 2 and 1 <= d and d <= 29:
        return True
    elif not is_leap(y) and m == 2 and 1 <= d and d <= 28:
        return True
    elif m in [1, 3, 5, 7, 8, 10, 12] and 1 <= d and d <= 31:
        return True
    elif m in [4, 6, 9, 11] and 1 <= d and d <= 30:
        return True
    return False

def what_season(y, m, d):
    if is_right_date(y, m, d):
        if m in [3, 4, 5]:
            return "Spring"
        elif m in [6, 7, 8]:
            return "Summer"
        elif m in [9, 10, 11]:
            return "Fall"
        elif m in [12, 1, 2]:
            return "Winter"
    else:
        return False


Y, M, D = map(int, input().split())
print(what_season(Y, M, D)) if what_season(Y, M, D) else print("-1")