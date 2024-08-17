n, m, k = map(int ,input().split())
penalty = [0] + [k for _ in range(1, n+1)]  # 벌칙 몇 번 남았는지 count

student = 0
for i in range(m):
    num = int(input())
    penalty[num] -= 1  # 벌칙 받는 학생의 number에서 -1
    if penalty[num] == 0:  # 학생의 남은 횟수가 0이 되면 학생의 number 찾기
        student = (penalty[1:].index(0) + 1)
        break

print(-1) if student == 0 else print(student)