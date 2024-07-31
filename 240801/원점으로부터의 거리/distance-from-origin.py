class Dot:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num


n = int(input())
arr = []
for i in range(1, n + 1):
    x, y = tuple(map(int, input().split()))
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    arr.append(Dot(x, y, i))

arr.sort(key=lambda x: x.x + x.y)
for d in arr:
    print(d.num)