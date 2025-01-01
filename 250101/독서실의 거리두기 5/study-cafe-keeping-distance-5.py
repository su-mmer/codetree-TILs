n = int(input())
arr = list(input())

max_zero = 0
for i in range(n):
    if arr[i] == '0':
        arr[i] = '1'  # 자리 init
        # print(arr.index('1'))
        # print(arr)
        cnt_zero = 0  # 0의 개수
        min_zero = 100  # 가장 가까운 거리
        for j in range(arr.index('1') + 1, n):  # 처음 찾은 1의 다음 자리부터 탐색
            if arr[j] == '1':
                min_zero = min(min_zero, cnt_zero + 1)
                cnt_zero = 0
            elif arr[j] == '0':
                cnt_zero += 1
            # print(j, cnt_zero, min_zero)
        arr[i] = '0'
        # print(min_zero)
    else:
        continue

    max_zero = max(max_zero, min_zero)

print(max_zero)