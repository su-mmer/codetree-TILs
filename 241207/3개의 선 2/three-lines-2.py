n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

flag = 0
i = 0
while(flag == 0 and i <= 10):
    j = 0
    while(flag == 0) and j <= 10:
        k = 0
        while(flag == 0 and k <= 10):
            count = 0
            for x in range(n):
                if arr[x][0] == i or arr[x][0] == j or arr[x][0] == k or arr[x][1] ==i or arr[x][1] == j or arr[x][1] == k:
                    count += 1
            if count == n:
                flag = 1
            else:
                flag = 0
            k += 1
        j += 1
    i += 1
print(flag)