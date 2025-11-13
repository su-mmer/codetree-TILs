n = int(input())

class Distance():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

distances = []
for i in range(n):
    x, y = map(int, input().split())
    distances.append(Distance(abs(x), abs(y), i+1))

distances.sort(key=lambda k : k.x + k.y)
for d in distances:
    print(d.num)