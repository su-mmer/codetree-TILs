n = int(input())
arr = [[] for _ in range(100001)]
p = 0

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == "R":
        for i in range(p,p+x):
            arr[i] += 'b'
            # print(arr[i])
        p += (x - 1)
    elif direction == "L":
        for i in range(p-x+1, p +1):
            arr[i] += 'w'
            # print(arr[i])
        p -= (x-1)

gray, white, black = 0, 0, 0
for i in range(len(arr)):
    if arr[i]==[]:
        continue
    elif arr[i].count('w') >= 2 and arr[i].count('b') >= 2:
        # print(arr[i])
        gray += 1
    elif arr[i][-1] == 'w':
        # print(arr[i])
        white += 1
    elif arr[i][-1] == 'b':
        # print(arr[i])
        black += 1

print(white, black, gray)