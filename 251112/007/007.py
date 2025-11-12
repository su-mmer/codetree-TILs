class Bonds:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

a, b, c = input().split()
james = Bonds(a, b, c)

print(f"secret code : {james.code}\nmeeting point : {james.place}\ntime : {james.time}")