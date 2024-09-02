n = int(input())
arr = list(input())

num = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] == 'C' and arr[j] == 'O' and arr[k] == 'W':
                num += 1

print(num)