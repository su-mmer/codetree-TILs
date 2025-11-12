n = int(input())
arr = list(map(int, input().split()))

arr.sort()

max_num = 0
for i in range(n):
    if max_num < arr[i] + arr[-i-1]:
        max_num = arr[i] + arr[-i-1]

print(max_num)