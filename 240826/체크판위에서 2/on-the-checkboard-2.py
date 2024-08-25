r, c = map(int, input().split())
arr = [list(input().split()) for _ in range(r)]

num = 0
for i in range(r):
    for j in range(c):
        if arr[0][0] != arr[i][j]:  # 첫번째와 다른 색 찾음
            for k in range(i+1, r-1):  # 범위가 (마지막-1)이어야 함
                for l in range(j+1, c-1):
                    if arr[i][j] != arr[k][l]:  # 두번째와 다른 색 찾음
                        num += 1

print(num)