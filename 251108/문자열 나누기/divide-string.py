n = int(input())
arr = input().split()

s = ''
for elem in arr:
    s += ''.join(elem)

n = 0
for elem in s:
    print(elem, end='')
    n += 1
    if n == 5:
        print()
        n = 0