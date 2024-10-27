n = int(input())
arr = list(map(int, input().split()))

cnt = 0  # 결과 개수
for i in range(n):
    for j in range(i, n):
        part_sum = 0
        for k in range(i, j+1):
            part_sum += arr[k]
        avg, div = divmod(part_sum, j-i+1)  # 평균 계산
        if div == 0 and avg in arr[i:j+1]:  # 나머지가 1이고 몫이 구간에 속하면
            cnt += 1

print(cnt)