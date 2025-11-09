#  윤년 판단
def is_year(n):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 4 == 0:
        return True
    return False


y = int(input())

print("true") if is_year(y) else print("false")