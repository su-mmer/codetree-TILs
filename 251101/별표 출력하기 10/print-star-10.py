n = int(input())

cnt_even, cnt_odd = 1, n

# 절반 출력
for i in range(n):
    if i % 2 == 0:
        for j in range(cnt_even):
            print("*", end=' ')
        cnt_even += 1
    else:
        for j in range(cnt_odd):
            print("*", end=' ')
        cnt_odd -= 1
    print()

# 나머지 절반 출력
if n % 2 == 0:  # n이 짝수일 경우
    for i in range(n):
        if i % 2 == 0:
            for j in range(cnt_even):
                print("*", end=' ')
            cnt_even += 1
        else:
            for j in range(cnt_odd):
                print("*", end=' ')
            cnt_odd -= 1
        print()
else:  # n이 홀수일 경우
    cnt_even, cnt_odd = cnt_odd, cnt_even 
    for i in range(n):
        if i % 2 == 0:
            for j in range(cnt_even):
                print("*", end=' ')
            cnt_even -= 1
        else:
            for j in range(cnt_odd):
                print("*", end=' ')
            cnt_odd += 1
        print()