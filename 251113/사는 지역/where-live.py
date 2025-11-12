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
for i in range(n-1):
    if people[i].name < people[i+1].name:
        num = i+1

print(f"name {people[num].name}\naddr {people[num].address}\ncity {people[num].region}")