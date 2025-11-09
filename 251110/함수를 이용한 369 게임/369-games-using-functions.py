def is_three(n):
    return n % 3 == 0

def is_my_answer(n):
    return '3' in str(n) or '6' in str(n) or '9' in str(n) or is_three(n)


a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if is_my_answer(i):
        cnt += 1

print(cnt)