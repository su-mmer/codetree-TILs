n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    m, tmp = i, i
    for j in range(i+1, n):
        if arr[j] < arr[m]:
            m = j
            # tmp = 
    arr[i], arr[m] = arr[m], arr[i]

for i in arr:
    print(i, end=' ')