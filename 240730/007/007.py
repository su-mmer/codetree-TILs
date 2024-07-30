class Thief:
    def __init__(self, s, m, t):
        self.code = s
        self.meeting = m
        self.time = t

s, m, t = tuple(input().split())
Thief1 = Thief(s, m, t)

print("secret code :", Thief1.code)
print("meeting point :", Thief1.meeting)
print("time :", Thief1.time)