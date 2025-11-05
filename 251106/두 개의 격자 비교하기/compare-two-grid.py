n, m = map(int, input().split())
a_arr = [ list(map(int, input().split())) for _ in range(n) ]
b_arr = [ list(map(int, input().split())) for _ in range(n) ]
new_arr = [ [0 for _ in range(m)] for _ in range(n) ]

# 새로운 배열 생성
for i in range(n):
    for j in range(m):
        new_arr[i][j] = 0 if a_arr[i][j] == b_arr[i][j] else 1

# 새로운 배열 출력
for row in new_arr:
    for elem in row:
        print(elem, end=' ')
    print()