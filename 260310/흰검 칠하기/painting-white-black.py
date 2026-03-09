n = int(input())
index_size=1000*100*2+2
block = [0 for _ in range(index_size)]
white_list = [0 for _ in range(index_size)]
black_list = [0 for _ in range(index_size)]

p = 1000*100  # first init
for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':  # x R
        for i in range(p, p+x):
            block[i] = 'B'
            black_list[i] += 1
        p += x-1
    elif d == 'L':  # x L
        for i in range(p, p-x, -1):
            block[i] = 'W'
            white_list[i] += 1
        p -= x-1
        
g, w, b = 0, 0, 0
for i in range(index_size):
    if white_list[i] >= 2 and black_list[i] >= 2:  # gray
        g += 1
    elif block[i] == 'W':  # white
        w += 1
    elif block[i] == 'B':  # black
        b += 1

print(w, b, g)
