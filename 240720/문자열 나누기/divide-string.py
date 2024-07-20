n = int(input())
string = input().split()
mystring = ''

for elem in string:
    mystring += ''.join(elem)

cnt = 0
for i in range(len(mystring)):
    print(mystring[i], end='')
    cnt += 1
    if cnt == 5:
        print('')
        cnt = 0