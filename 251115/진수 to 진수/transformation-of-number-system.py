a, b = map(int, input().split())
n = input()

# 십진수 변환
num = 0
for i in n:
    num = num * a + int(i)

# b진수 변환
digits = []
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

# 출력
for i in digits[::-1]:
    print(i, end='')