n, m = map(int, input().split())
arr_a = [0 for _ in range(50000)]
arr_b = [0 for _ in range(50000)]

# a 움직임 기록
move_a = 0
for _ in range(n):
    t, d = input().split()
    t = int(t)

    for i in range(t):
        move_a += 1
        arr_a[move_a] = arr_a[move_a-1] + (1 if d == 'R' else -1)

# b 움직임 기록
move_b = 0
for _ in range(m):
    t, d = input().split()
    t = int(t)

    for i in range(t):
        move_b += 1
        arr_b[move_b] = arr_b[move_b-1] + (1 if d == 'R' else -1)

# 최대 시간 만큼 머무르는 지점 저장
time = move_a if move_a > move_b else move_b
# print(arr_a[move_a+1])
if move_a < move_b:
    for i in range(move_a+1, time+1):
        arr_a[i] = arr_a[move_a]

if move_b < move_a:
    for i in range(move_b+1, time+1):
        arr_b[i] = arr_b[move_b]
     
# 바로 직전에는 다른 위치에 있다가 그 다음에 같은 위치에 오는 횟수
cnt = 0
for i in range(1, time+1):
    if arr_a[i] == arr_b[i] and arr_a[i-1] != arr_b[i-1]:
        cnt += 1
    
print(cnt)