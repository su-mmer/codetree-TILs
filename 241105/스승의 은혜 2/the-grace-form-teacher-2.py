n, budget = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

max_cnt = 0
for i in range(n):
    temp_arr = arr[:]
    temp_arr[i] = arr[i] // 2
    sum_val = 0
    for j in range(n):
        # print(temp_arr)
        sum_val += temp_arr[j]
        # print(temp_arr[j])
        if sum_val > budget:
            cnt = j
            break
    max_cnt = max(cnt, max_cnt)
print(max_cnt)