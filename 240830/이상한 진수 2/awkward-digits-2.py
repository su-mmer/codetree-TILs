# 한 숫자를 바꾼 거니까 한 자리씩 0,1 스위칭해서 제일 큰 값 찾기
digit = input()

max_num = 0
for i in range(len(digit)):
    change = list(digit)
    change[i] = "1" if digit[i] == "0" else "0"  # 숫자 하나 바꾼 change

    num = 0
    for n in change:
        num = num * 2 + int(n)  # 10진수 변환
    max_num = max(max_num, num)  # 더 큰 값

print(max_num)