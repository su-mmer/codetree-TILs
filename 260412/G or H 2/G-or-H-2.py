n = int(input())
arr = [0] * 101

max_location = 0
for i in range(n):
    location, alphabet = input().split()
    arr[int(location)] = alphabet
    max_location = max(max_location, int(location))  # 최대 위치 찾기

max_size = 0
for i in range(max_location - 1):  # 시작점
    for j in range(i + 2, max_location + 1):  # 끝점, 사람 2명 이상
        if not arr[i] == 0 and not arr[j] == 0:  # 시작, 끝에 사람이 있으면 
            cnt_g, cnt_h = 0, 0
            for k in range(i, j + 1):  # 시작~끝 사이의 h, g 찾기
                if arr[k] == 'G':
                    cnt_g += 1
                elif arr[k] == 'H':
                    cnt_h += 1
            if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
                size = j - i

            max_size = max(max_size, size)

print(max_size)