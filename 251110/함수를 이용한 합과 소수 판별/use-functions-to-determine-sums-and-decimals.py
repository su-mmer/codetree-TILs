def is_even(n):
    return (n % 10 + n // 10) % 2 == 0 

def is_answer(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag and is_even(n)


a, b = map(int, input().split())
cnt = 0
for n in range(a, b+1):
    if is_answer(n):
        cnt += 1

print(cnt)