a = input()
b = input()

a = list(a)
b = list(b)

if sorted(a) == sorted(b):
    print("Yes")
else:
    print("No")