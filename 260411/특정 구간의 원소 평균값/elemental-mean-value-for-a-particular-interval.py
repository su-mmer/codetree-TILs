n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        num = sum(arr[i:j+1]) / len(arr[i:j+1])  # 평균 계산

        if num in arr:  # 배열의 원소라면
            cnt += 1

print(cnt)