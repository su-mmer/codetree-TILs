a = input()
queries = input()

for i in queries:
    if i == 'L':
        a = a[1:] + a[0]
    elif i == 'R':
        a = a[-1] + a[:-1]

print(a)