def is_part(n1, n2):
    cnt = 0
    for i in range(n1-n2+1):
        if a[i:i+n2] == b:
            return True
    return False


n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print("Yes") if is_part(n1, n2) else print("No")