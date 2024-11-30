x, y = tuple(map(int, input().split()))

count = 0  # 팰린드롬 갯수
for i in range(x, y + 1):
    number = str(i)
    flag = True

    for n in range(len(number) // 2):
        if number[n] != number[-(n + 1)]:
            flag = False  # 다른 값을 찾으면 False로 변경하고 나가기
            break
        
    if flag == True: 
        count += 1

print(count)