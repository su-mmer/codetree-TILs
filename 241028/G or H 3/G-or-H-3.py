n, k = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
placed = [0 for _ in range(10001)]

for i in range(n):
    if arr[i][1] == 'G':
        placed[int(arr[i][0])] = 1
    if arr[i][1] == 'H':
        placed[int(arr[i][0])] = 2
# print(placed)
max_sum = 0
for i in range(1, len(placed)-k):
    mini_sum = 0
    for j in range(k+1):
        mini_sum += placed[i+j]
    max_sum = max(mini_sum, max_sum)

print(max_sum)