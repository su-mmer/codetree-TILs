n = int(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]  # 동남서북
mappers = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}

x, y = 0, 0  # 처음 위치
dir_num = 0  # 방향
cnt = 0  # 움직인 시간
flag = False  # 시작점인지 판별

for _ in range(n):
    v, d = input().split()  # 이동 방향, 이동 거리
    dir_num = mappers[v]

    for i in range(int(d)):
        x, y = x + dxs[dir_num], y + dys[dir_num]  # 한 칸 이동
        cnt += 1  # 1초 증가
        if x == 0 and y == 0:  # 시작점이면
            flag = True
            break  # 중단
    
    if flag: break  # 반복문 중지

print(cnt) if flag else print(-1)