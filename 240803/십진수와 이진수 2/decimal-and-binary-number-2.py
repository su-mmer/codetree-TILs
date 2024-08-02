n = input()
decimal = 0  # 십진수 담을 변수

# 십진수 변환
for i in range(len(n)):
    decimal = decimal * 2 + int(n[i])

# 17배
decimal *= 17

binary = []  # 이진수 담을 리스트
# 이진수 변환
while True:
    if decimal < 2:
        binary.append(decimal)
        break

    binary.append(decimal % 2)
    decimal //= 2

# 출력
for elem in binary[::-1]:
    print(elem, end='')