class Students():
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

students = []
for i in range(5):
    name, tall, weight = input().split()
    tall, weight = int(tall), float(weight)
    students.append(Students(name, tall, weight))

students.sort(key=lambda x: x.name)
print("name")
for s in students:
    print(s.name, s.tall, s.weight)
print()
students.sort(key=lambda x: -x.tall)
print("height")
for s in students:
    print(s.name, s.tall, s.weight)