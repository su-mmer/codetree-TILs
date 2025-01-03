n = int(input())
arr = list(input())

max_cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == '0' and arr[j] == '0':
            arr[i], arr[j] = '1', '1'
            cnt = 0
            min_cnt = 101
            for d in range(n):
                if arr[d] == '0':
                    cnt += 1
                elif arr[d] == '1' and d != 0:
                    min_cnt = min(min_cnt, cnt + 1)
                    cnt = 0
            arr[i], arr[j] = '0', '0'
            # print(min_cnt)
            max_cnt = max(max_cnt, min_cnt)

print(max_cnt)