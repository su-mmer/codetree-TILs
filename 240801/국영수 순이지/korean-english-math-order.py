class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


n = int(input())
student = []
for _ in range(n):
    name, kor, eng, math = input().split()
    student.append(Student(name, int(kor), int(eng), int(math)))

student.sort(key = lambda x: (-x.kor, -x.eng, -x.math))
for s in student:
    print(s.name, s.kor, s.eng, s.math)