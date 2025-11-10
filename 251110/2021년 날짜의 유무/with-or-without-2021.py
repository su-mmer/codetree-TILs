def is_date(m, d):
    if m == 2 and 1 <= d and d <= 28:
        return True
    elif m in [1, 3, 5, 7, 8, 10, 12] and 1 <= d and d <= 31:
        return True
    elif m in [4, 6, 9, 11] and 1 <= d and d <= 30:
        return True
    return False


M, D = map(int, input().split())
print("Yes") if is_date(M, D) else print("No")