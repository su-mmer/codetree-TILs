def calculate(a, o, c):
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '*':
        return a * c
    elif o == '/':
        return a // c
    else:
        return False


a, o, c = input().split()
a = int(a)
c = int(c)

if calculate(a, o, c):
    print(f"{a} {o} {c} = {calculate(a, o, c)}")
else:
    print("False")