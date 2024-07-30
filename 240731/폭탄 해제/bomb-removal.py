class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second


code, color, second = tuple(input().split())
b = Bomb(code, color, second)

print(f'code : {b.code}')
print(f'color : {b.color}')
print(f'second : {b.second}')