n = int(input())

for i in range(n):  # 3
    for j in range(n-i-1):  # 2
        print("", end=" ")
    for j in range(i+1):  # 1
        print("*", end=' ')
    print()

for i in range(n-1, -1, -1):  # n - i 
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end=' ')
    print()