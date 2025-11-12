class Character:
    def __init__(self, ids="codetree", lv=10):
        self.ids = ids
        self.lv = lv
    
a, b = input().split()
character1 = Character()
character2 = Character(a, b)

print(f"user {character1.ids} lv {character1.lv}")
print(f"user {character2.ids} lv {character2.lv}")