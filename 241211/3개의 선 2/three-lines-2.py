n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

flag = False  # 판별 flag
set_x, set_y = set(), set()  # x점 집합, y점 집합

for i in range(n):
    set_x.add(arr[i][0])

for i in range(n):
    set_y.add(arr[i][1])

# x, y 집합의 길이가 3이하이면 무조건 가능
if len(set_x) <= 3:
    flag = True

if len(set_y) <= 3:
    flag = True

list_x, list_y = list(set_x), list(set_y)
# x x y 탐색
for x1 in range(len(list_x)):
    for x2 in range(len(list_x)):
        for y in range(len(list_y)):
            for i in range(n):
                if arr[i][0] == x1 or arr[i][0] == x2 or arr[i][1] == y:
                    flag = True
# x y y 탐색
for x in range(len(list_x)):
    for y1 in range(len(list_y)):
        for y2 in range(len(list_y)):
            for i in range(n):
                if arr[i][0] == x or arr[i][1] == y1 or arr[i][1] == y2:
                    flag = True

print(int(flag))