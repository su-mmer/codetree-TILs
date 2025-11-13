n = int(input())

class Students():
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

students = []
for _ in range(n):
    name, tall, weight = input().split()
    tall, weight = int(tall), int(weight)

    students.append(Students(name, tall, weight))

students.sort(key = lambda x : (x.tall, -x.weight))
for s in students:
    print(s.name, s.tall, s.weight, sep=' ')