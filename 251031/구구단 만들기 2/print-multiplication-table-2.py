a, b = map(int, input().split())

for i in range(2, 10, 2):
    for j in range(b, a-1, -1):
        if j == a:
            print(f"{j} * {i} = {i * j}", end='')
        else:    
            print(f"{j} * {i} = {i * j}", end=' / ')
    print()