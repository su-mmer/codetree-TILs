n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

max_val = 0
for f_i in range(n):
    for f_j in range(n):
        # 오른 쪽에 범위가 있을 경우
        s_i = f_i
        for s_j in range(f_j+3, n):
            if not in_range(f_i, s_j+2):
                break
            
            val = arr[f_i][f_j] + arr[f_i][f_j+1] + arr[f_i][f_j+2] + arr[s_i][s_j] + arr[s_i][s_j+1] + arr[s_i][s_j+2]
            max_val = max(val, max_val)
        # 아래 쪽에 범위가 있을 경우
        for s_i in range(f_i+1, n):
            for s_j in range(n):
                if not in_range(s_i, s_j+2) or not in_range(f_i, f_j+2):
                    break
                
                val = arr[f_i][f_j] + arr[f_i][f_j+1] + arr[f_i][f_j+2] + arr[s_i][s_j] + arr[s_i][s_j+1] + arr[s_i][s_j+2]
                max_val = max(val, max_val)

print(max_val)