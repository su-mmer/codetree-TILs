# x로 시작해서 값에 2를 곱하는 것을 n번 반복, x찾기
n = int(input())
arr = [ tuple(map(int, input().split())) for _ in range(n)]
s, e = arr[0][0] // 2, arr[0][1] // 2

for i in range(s, e + 1):
    x = i
    flag = True
    for a, b in arr:
        x *= 2
        if x < a or b < x:
            flag = False
            break

    if flag:
        print(i)
        break