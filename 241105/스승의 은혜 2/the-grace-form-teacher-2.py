n, budget = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

max_cnt = 0
# for i in range(n):
#     cnt = 0
#     sum_val = 0
#     for j in range(n):
#         if i == j:
#             temp_arr = arr[:]
#             temp_arr[j] = arr[j] // 2
#         for k in range(n):
#             # print(temp_arr)
#             sum_val += temp_arr[k]
#             if sum_val > budget:
#                 cnt = k -1
#     max_cnt = max(cnt, max_cnt)

# print(max_cnt)

for i in range(n):
    temp_arr = arr[:]
    temp_arr[i] = arr[i] // 2
    sum_val = 0
    for j in range(n):
        sum_val += temp_arr[j]
        # print(temp_arr[j])
        if sum_val > budget:
            cnt = j
    max_cnt = max(cnt, max_cnt)
print(max_cnt)