a, b = map(int, input().split())
n = input()
decimal = 0 # 십진수 담을 변수

# n을 십진수로 변환
for i in range(len(n)):
    decimal = decimal * a + int(n[i])

digits = []  # b진수 담을 변수
# b진수 변환
while True:
    if decimal < b:
        digits.append(decimal)
        break

    digits.append(decimal % b)
    decimal //= b

for elem in digits[::-1]:
    print(elem, end='')