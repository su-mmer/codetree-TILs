n = int(input())
arr = [[] for _ in range(100001)]
p = 0

for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == "R":
        for i in range(p,p+x):
            arr[i] += 'b'
        p += (x - 1)
    elif direction == "L":
        for i in range(p-x+1, p +1):
            arr[i] += 'w'
        p -= (x-1)

white, black = 0, 0
for i in range(len(arr)):
    if arr[i] == []:
        continue
    elif arr[i][-1] == 'w':
        white += 1
    elif arr[i][-1] == 'b':
        black += 1

print(white, black)