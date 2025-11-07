a = input()
b = input()
c = input()

len_a = len(a)
len_b = len(b)
len_c = len(c)

if len_a < len_b and len_c < len_b:
    if len_a < len_c:
        print(len_b - len_a)
    else:
        print(len_b - len_c)
elif len_a < len_c and len_b < len_c:
    if len_a < len_b:
        print(len_c - len_a)
    else:
        print(len_c - len_b)
else:
    if len_b < len_c:
        print(len_a - len_b)
    else:
        print(len_a - len_c)