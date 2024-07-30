class People:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city


n = int(input())
peoples=[]
for _ in range(n):
    name, address, city = tuple(input().split())
    peoples.append(People(name, address, city))

index = n-1
for i in range(n-1):
    if peoples[index].name < peoples[i].name:
        index = i

print(f'name {peoples[index].name}')
print(f'addr {peoples[index].address}')
print(f'city {peoples[index].city}')