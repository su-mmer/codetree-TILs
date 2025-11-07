string = input()
string = list(string)

s = string[1]
for i, char in enumerate(string):
    if char == s:
        string[i] = string[0]

print(''.join(string))