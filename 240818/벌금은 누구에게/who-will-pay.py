n, m, k = map(int ,input().split())
# student = [0] + [i for i in range(1, n+1)]
penalty = [0] + [k for _ in range(1, n+1)]

student = 0
for i in range(m):
    num = int(input())
    penalty[num] -= 1
    if penalty[num] == 0:
        student = (penalty[1:].index(0) + 1)
        break
        
if student == 0:
    print(-1)
else:
    print(student)