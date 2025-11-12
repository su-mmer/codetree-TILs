n = int(input())
arr = list(map(int, input().split()))

arr.sort()
if arr[0] + arr[-1] < arr[n] + arr[n-1]:
    print(arr[n] + arr[n-1])
else:
    print(arr[0] + arr[-1])