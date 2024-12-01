n, k = map(int, input().split())
arr = list(int(input()) for _ in range(n))

bomb = -1  # 터지는 폭탄의 번호
for i in range(n - 3):
    if i+k+1 >= n:
        last = n
    else:
        last = i + k + 1

    for j in range(i + 1, last):
        if arr[i] == arr[j]:  # 거리 내에 같은 번호가 있으면 터짐
            bomb = max(bomb, arr[i])
            break

print(bomb)