n, k = map(int, input().split())
arr = [ int(input()) for _ in range(n) ]
number = [0] * 1000001  # 터진 폭탄 갯수 세기
bomb = [False] * n  # 터짐/안터짐 폭탄 표시

# 순서대로 돌면서 k범위 내에 있으면 number[i] += 1
for i in range(n - k):
    for j in range(i + 1, i + k + 1):  # 터진 폭탄 찾을 슬라이스
        if arr[i] == arr[j] and bomb[j] == False:  # 터진 폭탄 표시
            number[arr[i]] += 2
            bomb[i], bomb[j] = True, True
        
max_cnt, index = 0, 0  # 터진 폭탄 갯수, 터진 폭탄 번호
for i in range(len(number)-1, 0, -1):
    if max_cnt < number[i]:
        index = i
        max_cnt = number[i]
        
print(index)