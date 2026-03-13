n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans, legnth = 0, 0
for i in range(n):
    if arr[i] > t:
        length += 1
    else:
        length = 0
    
    if ans < length:
        ans = length

print(ans)