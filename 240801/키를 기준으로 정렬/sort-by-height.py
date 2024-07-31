class Size: 
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight


n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
s = [Size(name, tall, weight) for name, tall, weight in arr]

s.sort(key=lambda x: x.tall)

for person in s:
    print(person.name, person.tall, person.weight)