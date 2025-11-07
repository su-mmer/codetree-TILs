string = input()
string = list(string)

f, s = string[0], string[1]
for i in range(len(string)):
    if string[i] == f:
        string[i] = s
    elif string[i] == s:
        string[i] = f

print(''.join(string))