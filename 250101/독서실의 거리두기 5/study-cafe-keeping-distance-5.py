n = int(input())
arr = input()
arr = ['0'] + list(arr) + ['0']

max_zero = 0
for i in range(1, n + 1):
    # print(arr)
    # if arr[i-1] == '0' and arr[i] == '0' and arr[i+1] == '0':
    if arr[i] == '0':
        arr[i] = '1'  # 자리 init
        # print(arr)
        cnt_zero = 0  # 0의 개수
        min_zero = 100  # 가장 가까운 거리
        for j in range(1, n + 1):
            if arr[j] == '1' and j != 1:
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