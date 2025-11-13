n = int(input())

class Students():
    def __init__(self, tall, weight, num):
        self.tall = tall
        self.weight = weight
        self.num = num

students = []
for i in range(n):
    tall, weight = map(int, input().split())
    students.append(Students(tall, weight, i+1))

students.sort(key=lambda x : (-x.tall, -x.weight, x.num))
for s in students:
    print(s.tall, s.weight, s.num, sep=' ')