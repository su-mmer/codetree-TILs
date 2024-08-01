class Student:
    def __init__(self, height, weight, num):
        self.height, self.weight, self.num = height, weight, num


n = int(input())
student = []
for i in range(1, n+1):
    height, weight = tuple(input().split())
    student.append(Student(int(height), int(weight), i))

student.sort(key = lambda x: (x.height, -x.weight))

for s in student:
    print(s.height, s.weight, s.num)