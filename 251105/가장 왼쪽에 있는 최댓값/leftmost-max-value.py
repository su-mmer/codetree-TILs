n = int(input())
a = list(map(int, input().split()))

idx = n  # 가장 왼쪽의 최댓값 위치 초기화
while idx != 0:
    max_val = -1  # 최댓값 초기화
    # 가장 왼쪽의 최댓값 찾기
    for i in range(idx-1, -1, -1):
        if max_val <= a[i]:
            max_val = a[i]
            idx = i
    print(idx+1, end=' ')  # 최댓값 출력