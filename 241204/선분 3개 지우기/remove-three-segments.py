n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i == j or j == k or j == k:  # i, j, k는 항상 다른 수
                continue
            
            place = [0] * 101  # 선분의 위치
            flag = True
            for p in range(n):  # 선분 3개를 제외하고 겹치는지 판단
                if p == i or p == j or p == k:  # 제외할 3개의 선분
                    continue
                for e in range(arr[p][0], arr[p][1]+1):
                    # print(place[e])
                    if place[e] == 1:  # 겹침
                        flag = False
                        break
                    else:  # 안 겹침
                        place[e] = 1
            if flag == True:  # 안 겹치는 경우 counting
                count += 1

print(count)