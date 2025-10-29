arr = [int(input()) for x in range(5)]
satisfied = True

for i in arr:
    if i % 3 != 0:
        satisfied = False

print(1) if satisfied else print(0)