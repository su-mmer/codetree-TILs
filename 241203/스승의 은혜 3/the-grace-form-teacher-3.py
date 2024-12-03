n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

max_student = 0
for i in range(n):  # 쿠폰 쓸 학생
    cost, cnt = 0, 0  # 쿠폰 써서 더한 값, 학생 수
    for j in range(n):  # 최대 명수 계산
        if i == j:  # i==j 번째이면 pass
            continue
        cost += arr[j][1]
        if cost > b:
            break
        cnt += 1
    max_student = max(max_student, cnt)  # 최대 학생 수

print(max_student)