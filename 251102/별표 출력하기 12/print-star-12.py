n = int(input())

for i in range(n):
    # first line
    if i == 0:
        for j in range(n):
            print("*", end=' ')
        print()
    # begin second line ~ until line    
    else:
        # space
        for j in range(i - (i % 2) + 1):
            print(" ", end=' ')
        # star
        for j in range(i - (i % 2) + 1, n):
            if j % 2 != 0:
                print("*", end=" ")
            else:
                print(" ", end=' ')
        print()