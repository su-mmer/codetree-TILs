string = input()
string = list(string)

string[1] = 'a'
string[-2] = 'a'

string = ''.join(string)
print(string)