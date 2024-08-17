n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

count = 0
max_num = 0
for i in range(n):
    if i == 0:
        count += 1
    elif arr[i] < 0:
        if arr[i-1] < 0:
            count += 1
        elif arr[i-1] > 0:
            if max_num < count:
                max_num = count
                count = 1
    elif arr[i] > 0:
        if arr[i-1] > 0:
            count += 1
        elif arr[i-1] < 0:
            if max_num < count:
                max_num = count
                count = 1

if max_num == 0:
    max_num = count

print(max_num)