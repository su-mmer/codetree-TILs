n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

max_val = 0
for f_i in range(n):
    for f_j in range(n - 2):
        for s_i in range(n):
            for s_j in range(n -2):

                if f_i == s_i and abs(f_j - s_j) <= 2:  # 겹치는 경우 제외
                    continue

                val = arr[f_i][f_j] + arr[f_i][f_j+1] + arr[f_i][f_j+2] + arr[s_i][s_j] + arr[s_i][s_j+1] + arr[s_i][s_j+2]
                max_val = max(val, max_val)

print(max_val)