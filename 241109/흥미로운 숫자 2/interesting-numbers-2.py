x, y = map(int, input().split())

cnt = 0  # 흥미로운 숫자 counting
for num in range(x, y + 1):
    str_num = str(num)  # string 변환
    set_num = set(str_num)  # 집합 변환
    if len(set_num) == 2:  # 집합의 크기가 2일 때만 흥미로운 숫자 판별
        cnt_arr = [0, 0]
        a = tuple(set_num)[0]  # 숫자 a
        b = tuple(set_num)[1]  # 숫자 b
        for n in str_num:  # num 돌면서 각각 갯수 count
            if a == n :
                cnt_arr[0] += 1
            elif b == n:
                cnt_arr[1] += 1
        if cnt_arr[0] != 1 and cnt_arr[1] != 1:  # 둘다 1이 아니면 no interesting number
            continue
        else:
            cnt += 1
print(cnt)