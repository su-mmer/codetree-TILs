import sys

x = int(input())

# 1초마다 유지 / 1 증가 / 1감소 중 택 1
# 도착지에 도달하는 순간은 1m/s 최단 시간은?
min_time = sys.maxsize
for i in range(x):  # im부터 속도 줄이기 시작
    destination = x
    time = 0  # 걸린 시간
    val = 1  # 속도

    flag = False
    for j in range(x):
        if val == 0:
            val += 1
            time += 1
            destination -= val
            continue
        if destination <= 0 and val == 1:
            flag = True
            break
        elif destination <= 0 and val != 1:
            flag = False
            break
        
        if j < i:
            destination -= val
            val += 1
            time += 1
        elif i <= j and j < x:
    # for j in range(i+1, x):
            destination -= val
            val -= 1
            time += 1
        # print(time)
    if flag:
        # print(time)
        min_time = min(min_time, time)


print(min_time)