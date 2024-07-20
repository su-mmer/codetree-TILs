string, q = input().split()

for quest in range(int(q)):
    quest = int(input())
    if quest == 1:
        string = string[1:] + string[0]
    elif quest == 2:
        string = string[-1] + string[:-1]
    elif quest == 3:
        string = string[::-1]
    print(string)