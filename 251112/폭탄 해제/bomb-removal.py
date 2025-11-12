class Bomb ():
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

a, b, c = input().split()
bomb = Bomb(a, b, c)
print(f"code : {bomb.code}\ncolor : {bomb.color}\nsecond : {bomb.sec}")