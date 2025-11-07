string = input()
string = list(string)

while len(string) > 1:
    n = int(input())

    if n >= len(string):
        string.pop()
    else:
        string.pop(n)
    
    print(''.join(string))
