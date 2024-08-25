# 모든 사람들의 이동 거리의 합이 최소
import sys

n = int(input())
arr = list(map(int, input().split()))

min_diff = sys.maxsize  # 가장 큰 값
for i in range(n):
    sum_diff = 0  
    for j in range(n): # 모든 사람들의 이동 거리의 합 계산
        sum_diff += abs(i - j) * arr[j]
    
    min_diff = min(min_diff, sum_diff)  # 비교

print(min_diff)