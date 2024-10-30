n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# 첫번째에 해당 하는거 + 두 번째에 해당 하는 거 - 공집합
set_a1 = set()
for x in range(a1-2, a1+3):
    if x <= 0:
        x = n + x
    set_a1.add(x)
set_b1 = set()
for y in range(b1-2, b1+3):
    if y <= 0:
        y = n + y
    set_b1.add(y)
set_c1 = set()
for z in range(c1-2, c1+3):
    if z <= 0:
        z = n + z
    set_c1.add(z)

set_a2 = set()
for x in range(a2-2, a2+3):
    if x <= 0:
        x = n + x
    set_a2.add(x)
set_b2 = set()
for y in range(b2-2, b2+3):
    if y <= 0:
        y = n + y
    set_b2.add(y)
set_c2 = set()
for z in range(c2-2, c2+3):
    if z <= 0:
        z = n + z
    set_c2.add(z)

cnt = len(set_a1) * len(set_b1) * len(set_c1) + len(set_a2) * len(set_b2) * len(set_c2) - len(set_a1 & set_a2) * len(set_b1 & set_b2) * len(set_c1 & set_c2)
print(cnt)