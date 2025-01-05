n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]

flag = False
for i in range(n):
    overlap = [0] * 101  # 선분의 위치 저장

    for j in range(n):
        if i == j:
            continue

        for k in range(arr[j][0], arr[j][1] + 1):
            overlap[k] += 1
            
    for j in overlap:
        if j == n - 1:
            flag = True
            break

print("Yes") if flag else print("No")