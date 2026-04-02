n = int(input())
orders = input()

cnt = 0
for c in range(n):
    for o in range(c + 1, n):
        for w in range(o + 1, n):
            if orders[c] == "C" and orders[o] == "O" and orders[w] == "W":
                cnt += 1

print(cnt)