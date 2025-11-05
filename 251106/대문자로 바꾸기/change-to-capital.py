arr = [ input().split() for _ in range(5) ]

# print(ord('a'), ord('A'))
for i in range(5):
    for j in range(3):
        print(chr(ord(arr[i][j])-32), end=' ')
    print()