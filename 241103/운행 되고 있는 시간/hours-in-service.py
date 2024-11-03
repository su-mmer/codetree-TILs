n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_time = 0
for i in range(n):
    time = [0] * 1001
    for j in range(n):
        if j == i:
            continue
        # 운행 중인 시간에 1
        for k in range(arr[j][0], arr[j][1]):
            time[k] = 1
        max_time = max(max_time, sum(time))

print(max_time)