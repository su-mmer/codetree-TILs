n = int(input())

for i in range(11, 11+(n*2), 2):
    for j in range(i, i+(n*2), 2):
        print(j, end=' ')
    print()