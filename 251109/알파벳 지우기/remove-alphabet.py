a = input()
b = input()

a_num, b_num = '', ''
for c in a:
    if c.isdigit():
        a_num += c
for c in b:
    if c.isdigit():
        b_num += c

print(int(a_num) + int(b_num))