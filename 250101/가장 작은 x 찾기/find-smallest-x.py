# x로 시작해서 값에 2를 곱하는 것을 n번 반복, x찾기
n = int(input())
arr = [ tuple(map(int, input().split())) for _ in range(n)]
s, e = arr[0][0] // 2, arr[0][1] // 2

for i in range(s, e + 1):
    x = i
    flag = True
    for j in range(n):
        x *= 2
        if x < arr[j][0] or arr[j][1] < x:
            flag = False
            break

    if flag:
        print(i)
        break