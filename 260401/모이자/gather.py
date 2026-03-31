import sys

n = int(input())
A = list(map(int, input().split()))

answer = sys.maxsize

for i in range(n):
    sum_dis = 0
    for j in range(n):
        sum_dis += abs(i-j) * A[j]
    
    answer = min(answer, sum_dis)

print(answer)