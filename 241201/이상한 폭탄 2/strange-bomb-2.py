n, k = map(int, input().split())
arr = list(int(input()) for _ in range(n))

bomb = -1  # 터지는 폭탄의 번호
for i in range(n - 3):
    for j in range(1, k + 1):
        if arr[i] == arr[i + j]:  # 거리 내에 같은 번호가 있으면 터짐
            bomb = max(bomb, arr[i])
            break

print(bomb)