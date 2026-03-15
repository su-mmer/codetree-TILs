OFFSET = 1000
n, m = map(int, input().split())
arr_a = [0 for _ in range(OFFSET * n + 1)]
arr_b = [0 for _ in range(OFFSET * m + 1)]

def move(r, arr):
    global time
    p = 0
    # time = 0
    for _ in range(r):
        d, t = input().split()
        t = int(t)
        for _ in range(t):
            time += 1
            p += 1 if d == 'R' else -1
            arr[time] = p


time = 0
move(n, arr_a)

time = 0
move(m, arr_b)

# 답 출력
flag = False
for i in range(1, time+1):
    if arr_a[i] == arr_b[i]:
        print(i)
        flag = True
        break

if flag == False:
    print(-1)
