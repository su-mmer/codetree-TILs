string = input()
mystr = list(string)

mystr[1] = 'a'
mystr[-2] = 'a'
print(''.join(mystr))