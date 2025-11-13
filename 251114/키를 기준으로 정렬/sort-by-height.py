n = int(input())

class Student():
    def __init__ (self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight
    
students = []
for i in range(n):
    name, tall, weight = input().split()
    students.append(Student(name, tall, weight))

students.sort(lambda x : x.tall)

for s in students:
    print(s.name, s.tall, s.weight, sep=' ')
