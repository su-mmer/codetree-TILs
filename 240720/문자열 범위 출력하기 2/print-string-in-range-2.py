string = input()
n = int(input())

if n > len(string):
    print(string[::-1])
else:
    print(string[:-11:-1])