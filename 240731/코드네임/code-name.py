class Member:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score


members = []
for _ in range(5):
    codename, score = tuple(input().split())
    members.append(Member(codename, int(score)))

member, lower = members[4].codename, members[4].score
for i in range(4):
    if lower > members[i].score:
        lower = members[i].score
        member = members[i].codename

print(member, lower)