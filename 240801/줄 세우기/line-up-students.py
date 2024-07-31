class Student:
    def __init__(self, tall, weight, num):
        self.tall = tall
        self.weight = weight
        self.num = num


n = int(input())
student = []
for i in range(1, n + 1):
    tall, weight = tuple(input().split())
    student.append(Student(int(tall), int(weight), int(i)))

student.sort(key=lambda x: (-x.tall, -x.weight, x.num))
for s in student:
    print(s.tall, s.weight, s.num)