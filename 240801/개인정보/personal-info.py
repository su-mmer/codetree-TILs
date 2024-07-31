class People:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight


person = []
for _ in range(5):
    name, tall, weight = tuple(input().split())
    person.append(People(name, int(tall), weight))

person.sort(key=lambda x: x.name)
print("name")
for p in person:
    print(f'{p.name} {p.tall} {p.weight}')

print()

person.sort(key=lambda x: -x.tall)
print("height")
for p in person:
    print(f'{p.name} {p.tall} {p.weight}')