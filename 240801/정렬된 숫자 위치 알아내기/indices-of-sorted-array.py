class Sequence:
    def __init__(self, value, num):
        self.value = value
        self.num = num


n = int(input())
arr = list(map(int, input().split()))
sequence = []
for i in range(n):
    sequence.append(Sequence(arr[i], i+1))
sequence.sort(key=lambda x: x.value)

answer = [0] * (n + 1)
for idx, s in enumerate(sequence, start = 1):
    answer[s.num] = idx

for enum in answer[1:]:
    print(enum, end= ' ')