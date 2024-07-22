n = int(input())

def pirnt_star(n):
    if n == 0:
        return
    
    print("* " * n)
    pirnt_star(n - 1)
    print("* " * n)


pirnt_star(n)