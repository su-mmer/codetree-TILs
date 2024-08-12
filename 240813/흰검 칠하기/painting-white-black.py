n = int(input())
arr = [[] for _ in range(200001)]
p = 0
# OFFSET=100000

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == "R":
        # if p < 0:
        #     p += OFFSET
        for i in range(p, p+x):
            arr[i] += 'b'
            # print(arr[i])
        p += x
    elif direction == "L":
        for i in range(p-x, p):
            arr[i] += 'w'
            # print(arr[i])
        p -= x

gray, white, black = 0, 0, 0
# print(arr[-1])
for i in range(len(arr)):
    # print(arr[i])
    if arr[i]==[]:
        # print(arr[i])
        continue
    elif arr[i].count('w') >= 2 and arr[i].count('b') >= 2:
        gray += 1
    elif arr[i][-1] == 'w':
        white += 1
    elif arr[i][-1] == 'b':
        black += 1

print(white, black, gray)