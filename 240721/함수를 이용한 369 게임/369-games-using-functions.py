a, b = map(int, input().split())
cnt = 0

def is_3_6_9(i):
    while i > 0:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            return True
        i = i // 10


def is_multiple(i):
    return i % 3 == 0


for i in range(a, b+1):
    if is_3_6_9(i) or is_multiple(i):
        cnt += 1

print(cnt)