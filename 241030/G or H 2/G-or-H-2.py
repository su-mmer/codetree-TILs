n = int(input())
arr = [list(input().split()) for _ in range(n)]

for i in range(n):
    arr[i][0] = int(arr[i][0])

sorted_arr = sorted(arr)
# print(sorted_arr)
max_dist = 0
for i in range(n):
    alpha = sorted_arr[i][1]  # 기준 알파벳
    for j in range(i+1, n+1):
        num_1, num_2, num_3 = 0, 0, 0
        cnt_same_alph, cnt_ban_alpha = 0, 0
        for k in range(i, j): # G, H가 같은 개수인지 판별    # 0, 2
            if sorted_arr[k][1] == alpha:
                num_1 += 1
            elif sorted_arr[k][1] != alpha:
                num_2 += 1
        if num_1 == num_2: 
            cnt_ban_alpha = sorted_arr[j-1][0] - sorted_arr[i][0]
        for k in range(i, j):  # 기준 알파벳이 어디까지 같은지
            pv = k
            if sorted_arr[k][1] == alpha:
                num_3 += 1
            else:
                break
        cnt_same_alph = sorted_arr[pv][0] - sorted_arr[i][0]
        
        max_dist = max(cnt_ban_alpha, max_dist)
        max_dist = max(cnt_same_alph, max_dist)

print(max_dist)