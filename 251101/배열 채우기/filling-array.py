arr = list(map(int, input().split()))

cnt = 9
for i in range(len(arr)):
    if arr[i] == 0:
        cnt = i - 1
        break

for elem in arr[cnt::-1]:
    print(elem, end=' ')