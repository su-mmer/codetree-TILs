n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_student = 0  # 최대 학생 수
for i in range(n):  # 전체 학생
    cost, cnt = 0, 0  # 쿠폰 써서 더한 값, 학생 수
    half = []  # 반값 쿠폰 썼을 시 배열
    for j in range(n):  # 선물값 + 배송비
        if i == j:  # i==j 번째 학생한테 쿠폰
            half.append((arr[j][0] // 2) + arr[j][1])
        else:
            half.append(arr[j][0] + arr[j][1])
    half.sort()  # 저렴한 것부터
    for k in range(n):  # budget 초과 시 그만
        cost += (half[k])
        if cost > b:
            break
        cnt += 1
    max_student = max(max_student, cnt)  # 최대 학생 수

print(max_student)