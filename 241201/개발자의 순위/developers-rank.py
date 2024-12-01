k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 같은 개발자 번호면 pass
        if i == j:
            continue
        
        flag = True
        for game in arr:
            # i 가 j 보다 뒤에 있으면 후보 탈락
            if game.index(i) > game.index(j):
                flag = False
                break
        if flag == True:
            count += 1

print(count)