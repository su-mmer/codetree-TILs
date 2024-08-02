n, b = map(int, input().split())
digits = []

# 10진수 N을 B진수로 변경 -> 4진수 또는 8진수
while True:
    if n < b:
        digits.append(n)
        break

    digits.append(n % b)
    n //= b


for elem in digits[::-1]:
    print(elem, end='')