class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


n = int(input())
student = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    student.append(Student(name, int(height), int(weight)))

student.sort(key=lambda x: (x.height, -x.weight))
for s in student:
    print(s.name, s.height, s.weight)