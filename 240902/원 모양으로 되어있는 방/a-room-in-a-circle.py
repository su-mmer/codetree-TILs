import sys

n = int(input())
arr = [int(input()) for _ in range(n)]
num_arr = [i for i in range(n)]

INT_SIZE = sys.maxsize

min_dist = INT_SIZE

for i in range(n):
    dist = 0
    for j in range(n):  # 인원
        dist += arr[j] * num_arr[j]
    
    min_dist = min(min_dist, dist)
    num_arr = [num_arr[n-1]] + num_arr[:n-1]


print(min_dist)