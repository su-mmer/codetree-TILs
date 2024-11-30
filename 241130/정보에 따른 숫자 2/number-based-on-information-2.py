import sys
MAXSIZE = sys.maxsize
MINSIZE = -sys.maxsize
T, a, b = map(int, input().split())

arr = [0] * 1001
for i in range(T):
    alphabet, d = tuple(input().split())
    arr[int(d)] = alphabet

# left_s, left_n 시작점으로부터 왼쪽의 s, n 좌표
ls, ln, rs, rn = MINSIZE, MINSIZE, MAXSIZE, MAXSIZE
for i in range(a, 0, -1):
    if arr[i] == 'S':
        ls = i
        break
for i in range(a, 0, -1):
    if arr[i] == 'N':
        ln = i
        break
# right_s, right_n 시작점으로부터 오른쪽의 s, n 좌표
for i in range(a, len(arr)):
    if arr[i] == 'S':
        rs = i
        break
for i in range(a, len(arr)):
    if arr[i] == 'N':
        rn = i
        break

count = 0  # special 갯수
for x in range(a, b + 1):  # special 탐색
    if arr[x] == 'S':
        count += 1  # 무조건 special
        ls = x  # left_s 좌표 변경
        for next_x in range(x, b + 1):
            if arr[next_x] == 'S':
                rs = next_x  # right_s 좌표 변경
    elif x == 'N':
        continue  # 무조건 no special
        ln = x  # left_n 좌표 변경
        for next_x in range(x, b + 1):
            if arr[next_x] == 'N':
                rn = next_x  # right_n 좌표 변경
    else:
        dist_s = min(abs(ls - x), abs(rs - x))  # ls, rs 중 x와 가까운 거리
        dist_n = min(abs(ln - x), abs(rn - x))  # ln, rn 중 x와 가까운 거리

        if dist_s <= dist_n:  # special count
            count += 1
        # print(dist_s, dist_n)

print(count)