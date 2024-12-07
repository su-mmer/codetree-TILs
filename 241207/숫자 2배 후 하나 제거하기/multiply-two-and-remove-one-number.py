import sys

n = int(input())
arr = list(map(int, input().split()))

sum_min = sys.maxsize
for m in range(n):  # multiple 숫자
    arr[m] *= 2

    for e in range(n):  # 제거할 숫자

        erase = []  # 1개 제거한 배열
        for i in range(n):
            if i == e:
                continue
            erase.append(arr[i])

        sum_diff = 0  # 인접한 숫자의 차 계산
        for i in range(n - 2):
            sum_diff += abs(erase[i] - erase[i+1])
        
        sum_min = min(sum_diff, sum_min)

    arr[m] //= 2  # 2배 한 숫자 돌려놓기

print(sum_min)