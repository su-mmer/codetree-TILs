n, m = map(int, input().split())
arr_a = [0]
arr_b = [0]

p = 0
for _ in range(n):
    direct, meter = input().split()
    meter = int(meter)
    if direct == 'L':  # 1초마다 얼마나 이동하는지 추가
        for j in range(1, meter+1):
            arr_a.append(p - j)
        p -= j
    else:
        for j in range(1, meter+1):
            arr_a.append(p + j)
        p += j

p = 0
for _ in range(m):
    direct, meter = input().split()
    meter = int(meter)
    if direct == 'L':
        for j in range(1, meter+1):
            arr_b.append(p - j)
        p -= j
    else:
        for j in range(1, meter+1):
            arr_b.append(p + j)
        p += j

count = 0  # 결과
for i in range(1, min(len(arr_a), len(arr_b))):  # a와 b중 작은 배열의 길이까지만 비교
    if arr_a[i] == arr_b[i]:
        count = i
        break  # 같은 값 찾으면 반복문 끝

print(-1) if count == 0 else print(count)  # 같은 값이 있으면 출력, 없으면 -1