n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

cnt = 0
for i in range(n - m + 1):
    check = [0] * m  # 아름다운 수열 확인

    for k in range(i, i+m):  # arr_a에서 연속 부분 수열
        for j in range(m):  # arr_b의 원소와 비교
            if arr_a[k] == arr_b[j] and check[j] == 0:  # 연속 부분 수열이 b의 원소이고 중복되지 않으면
                check[j] = 1
                break  # 중복방지
                
    if sum(check) == m:
        cnt += 1

print(cnt)