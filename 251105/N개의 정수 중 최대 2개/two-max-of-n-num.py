import sys

n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
first, second = -sys.maxsize, -sys.maxsize
pv = 0
# 제일 큰 값 찾기
for i in range(n):
    if first < a[i]:
        first = a[i]
        pv = i

# 두번째 값 찾기
for i in range(n):
    if i == pv:  # 첫 번째 값이랑 같은 위치이면 비교하지 않고 패스
        continue
    if second < a[i]:
        second = a[i]

print(first, second, sep=' ')