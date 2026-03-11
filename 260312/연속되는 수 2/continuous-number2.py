n = int(input())
arr = [int(input()) for _ in range(n)]

cnt, max_cnt = 0, 0
for i in range(1, n):
    if arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnt = 0
    
    if cnt > max_cnt:
        max_cnt = cnt
    
print(max_cnt+1)        