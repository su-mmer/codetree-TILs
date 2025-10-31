n = int(input())

cnt='A'
for i in range(n):

    for j in range(i):
        print(' ', end=' ')

    for j in range(n-i):
        if ord(cnt) > ord('Z'):
            cnt = 'A'
        print(cnt, end=' ')

        cnt = chr(ord(cnt) + 1) 

    print()