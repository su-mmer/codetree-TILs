class Character:
    def __init__(self, user="codetree", lv=10):
        self.user = user
        self.lv = lv


user, lv = tuple(input().split())

c1 = Character()
c2 = Character(user, lv)
print(f'user {c1.user} lv {c1.lv}')
print(f'user {c2.user} lv {c2.lv}')