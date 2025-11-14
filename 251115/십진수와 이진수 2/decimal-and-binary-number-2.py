n = input()
num = 0

# 십진수 변환
for i in n:
    num = num * 2 + int(i)

num *= 17

# 이진수 변환
digits = []
while True:
    if num < 2:
        digits.append(num)
        break

    digits.append(num % 2)
    num //= 2

# 출력
for i in digits[::-1]:
    print(i, end='')