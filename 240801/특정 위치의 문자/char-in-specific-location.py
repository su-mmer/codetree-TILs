arr = ['L', 'E', 'B', 'R', 'O', 'S']

ch = input()
idx = -1

for i, char in enumerate(arr):
    if ch == char:
        idx = i

if i == -1:
    print("None")
else:
    print(idx)