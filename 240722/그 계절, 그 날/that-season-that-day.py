y, m, d = map(int, input().split())

# 윤년 판별
def is_yoon(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False


# 날짜가 존재하는지 판별
def is_date(y, m, d):
    if m == 2 and is_yoon(y):
        if 1 <= d and d <= 29:
            return True
    elif m == 2:
        if 1 <= d and d <= 28:
            return True
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= d and d <= 31:
            return True
    elif m in [4, 6, 9, 11]:
        if 1 <= d and d <= 30:
            return True
    return False


# 어느 계절인지 판별
def what_season(y, m, d):
    if m in [3, 4, 5]:
        return "Spring"
    elif m in [6, 7, 8]:
        return "Summer"
    elif m in [9, 10, 11]:
        return "Fall"
    else:
        return "Winter"


# 존재하는 날이라면 계절 판별, 아니면 -1
if is_date(y, m, d):
    print(what_season(y, m, d))
else:
    print(-1)