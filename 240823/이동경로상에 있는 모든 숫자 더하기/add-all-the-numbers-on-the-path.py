n, t = map(int, input().split())  # 정사각형 크기, 명령 횟수
orders = input()  # 명령
arr = [ list(map(int, input().split())) for _ in range(n) ]  # 격자

# 격자 벗어낫는지 판단
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 격자
x, y = n // 2, n // 2  # 가운데 위치
dir_num = 3  # 시작 방향(북쪽)
answer = arr[x][y]  # 시작 위치 값부터 포함

# 입력받은 명령에 따라 계산
for order in orders:
    if order == 'L':
        dir_num = (dir_num + 3) % 4
    elif order == 'R':
        dir_num = (dir_num + 1) % 4
    elif order == 'F':
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if in_range(nx, ny):  # 범위 내에 있으면 더함
            x, y = x + dxs[dir_num], y + dys[dir_num]
            answer += arr[x][y]

print(answer)