class Person():
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region


n = int(input())

people = []
for _ in range(n):
    name, add, reg = input().split()
    people.append(Person(name, add, reg))

num = 0
for i in range(n):
    if people[i].name > people[num].name:
        num = i

print(f"name {people[num].name}")
print(f"addr {people[num].address}")
print(f"city {people[num].region}")