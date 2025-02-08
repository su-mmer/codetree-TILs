n = int(input())
arr = list(input().split())

pos = len(max(arr, key=len))

for i in range(n):  # 0 붙이기
    if len(arr[i]) != pos:
        while len(arr[i]) != pos:
            arr[i] = '0' + arr[i]

while pos > 0:
    pos -= 1
    temp_arr = [[] for _ in range(10)]  # 0~9 정리할 배열

    for i in range(n):  # 각 기수의 순서에 맞게 배열에 넣기
        temp_arr[int(arr[i][pos])].append(arr[i])

    merge_arr = []  # 순서 합할 배열
    for i in range(10):  # 기수 순서에 맞게 정렬된 배열을 merge
        for j in range(len(temp_arr[i])):
            merge_arr.append(temp_arr[i][j])
    arr = merge_arr

for num in arr:  # 0 떼려고 정수 변환
    print(int(num), end=' ')