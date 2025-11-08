string = input()

result = ''
for char in string:
    # 대문자일 경우 그냥 추가
    if 'A' <= char and char <= 'Z':
        result += ''.join(char)
    # 소문자일 경우 대문자 변환
    elif 'a' <= char and char <= 'z':
        result += ''.join(chr(ord(char)-ord('a')+ord('A')))
    # 알파벳이 아닐 경우 패스
    else:
        continue

print(result)