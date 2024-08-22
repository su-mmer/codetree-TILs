# 이동할 위치가 격자 밖이거나 !=0이면 방향 전환 (dir_num + 1) % 4
# 이후에 알파벳 입력
# Z 다음에 A로 변환 필요

n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 격자
x, y = 0, 0  # 시작 위치
dir_num = 0  # 초기 방향(오른쪽)
arr[x][y] = ('A')  # 시작 위치의 값
for i in range(1, n * m):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = chr(ord('A')+(i % 26))  # 아스키변환 사용
    

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()