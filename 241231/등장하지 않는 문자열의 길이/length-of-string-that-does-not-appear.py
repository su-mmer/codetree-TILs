n = int(input())
arr = input()

for i in range(1, n + 1):  # 문자열 길이
    flag = True  # 1번인지 판독

    for j in range(n - i):
        origin = arr[j:j + i]  # 비교할 문자열
        if arr.count(origin) > 1:
            flag = False
            break
    if flag:  # 한 번만 발견된 문자열의 최소 길이
        ans = i
        break
print(ans)