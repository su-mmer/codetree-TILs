string = input()

def alphabet(string):
    ch = string[0]    
    for elem in string[1:]:
        if ch != elem:
            return True
    return False


if alphabet(string):
    print("Yes")
else:
    print("No")