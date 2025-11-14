n = int(input())
questions = [ list(input().split()) for _ in range(n) ]
OFFSET = 100 * n
count_white = [ 0 for _ in range(OFFSET * 2 + 1) ]
count_black = [ 0 for _ in range(OFFSET * 2 + 1) ]
color = [ False for _ in range(OFFSET * 2 + 1) ]  # tile color

# white 1, black 2, gray 3
pv = OFFSET
for q in questions:
    q[0] = int(q[0])
    
    if q[1] == "L":
        for i in range(pv, pv-q[0], -1):
            count_white[i] += 1
            if count_white[i] >= 2 and count_black[i] >= 2:
                color[i] = "G"
            if color[i] != "G":
                color[i] = "W"
        pv = pv - q[0] + 1  # 현재 타일부터 시작하도록 
    elif q[1] == "R":
        for i in range(pv, pv+q[0]):
            count_black[i] += 1
            if count_white[i] >= 2 and count_black[i] >= 2:
                color[i] = "G"
            if color[i] != "G":
                color[i] = "B"
        pv = pv + q[0] - 1  # 현재 타일부터 시작하도록

w, b, g = 0, 0, 0
for c in color:
    if c == "W":
        w += 1
    elif c == "B":
        b += 1
    elif c == "G":
        g += 1

print(w, b, g, end=' ')