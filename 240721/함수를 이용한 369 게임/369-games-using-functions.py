a, b = map(int, input().split())
cnt = 0

def is_3_6_9(i):
    while True:
        quot, remain = i // 10, i % 10
        if remain == 3 or remain == 6 or remain == 9:
            return True
        if quot < 1:
            return False
        i = quot


def is_multiple(i):
    return i % 3 == 0


for i in range(a, b+1):
    if is_3_6_9(i) or is_multiple(i):
        cnt += 1

print(cnt)