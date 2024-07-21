y, m, d = map(int, input().split())

# 윤년 판별
def is_leap(y):
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    if y % 400 == 0:
        return True
    return False


# 날짜가 존재하는지 판별
def is_date(y, m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days[2] = 29 if is_leap(y) else 28
    return d <= days[m]


# 존재하는 날이라면 계절 판별, 아니면 -1
if is_date(y, m, d):
    if 3 <= m and m <= 5:
        print("Spring")
    elif 6 <= m and m <= 8:
        print("Summer")
    elif 9 <= m and m <= 11:
        print("Fall")
    else:
        print("Winter")
else:
    print(-1)