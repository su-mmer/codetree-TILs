n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        space = arr[i:j+1]
        avg = sum(space) / len(space)  # 평균 계산

        if avg in space:  # 배열의 원소라면
            cnt += 1

print(cnt)