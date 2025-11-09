cnt = 0  # 문자열의 총 개수
arr = []

while True:
    string = input()

    # 탈출 조건
    if string == '0':
        break
    
    # 문자열 개수
    cnt += 1
    # 홀수 번째
    if cnt % 2 != 0:
        arr.append(string)

# 출력
print(cnt)
for elem in arr:
    print(elem)