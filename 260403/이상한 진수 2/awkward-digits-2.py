str_a = input()

max_cnt = 0
for i in range(len(str_a)):
    part = str_a[:i]+str(1 - int(str_a[i]))+str_a[i+1:]  # 0 <-> 1
    part = int(part)

    num = 0
    for j in range(len(str_a)):  # 이진수 -> 십진수
        num = num + part % 10 * (2 ** j)
        part = part // 10

    max_cnt = max(num, max_cnt)  # 제일 큰 수

print(max_cnt)