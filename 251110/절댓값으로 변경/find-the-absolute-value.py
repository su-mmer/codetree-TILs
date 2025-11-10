def change_absolute(arr, n):
    for i in range(n):
        arr[i] = abs(arr[i])


n = int(input())
arr = list(map(int, input().split()))

change_absolute(arr, n)
for elem in arr:
    print(elem, end=' ')