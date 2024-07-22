n = int(input())
arr = list(map(int, input().split()))

def absolute():
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]

absolute()
for elem in arr:
    print(elem, end=' ')