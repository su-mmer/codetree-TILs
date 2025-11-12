import sys

class Agent():
    def __init__(self, codename, score):
        self.codename = codename
        self.score = int(score)

agent = []
for _ in range(5):
    codename, score = input().split()
    agent.append(Agent(codename, score))

min_score = sys.maxsize
min_agent = 0
for a in agent:
    if a.score < min_score:
        min_score = a.score
        min_agent = a

print(min_agent.codename, min_agent.score)