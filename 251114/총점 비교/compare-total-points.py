n = int(input())

class Students():
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

students = []
for _ in range(n):
    name, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    
    students.append(Students(name, a, b, c))

students.sort(key=lambda x: x.a + x.b + x.c)

for s in students:
    print(s.name, s.a, s.b, s.c, sep=' ')