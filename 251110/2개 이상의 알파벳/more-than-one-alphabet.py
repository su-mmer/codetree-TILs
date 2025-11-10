def is_over_two(a):
    pv = a[0]
    for i in a[1:]:
        if pv != i:
            return True
    return False


a = input()
print("Yes") if is_over_two(a) else print("No")