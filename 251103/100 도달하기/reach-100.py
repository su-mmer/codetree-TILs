n = int(input())
arr = [0 for _ in range(100)]

arr[0], arr[1] = 1, n
for i in range(2, 100):
    arr[i] = arr[i-1] + arr[i-2]
    if arr[i] > 100 :
        break

for elem in arr:
    if elem == 0:
        break
    print(elem, end=' ')