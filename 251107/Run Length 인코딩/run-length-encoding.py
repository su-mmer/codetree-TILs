a = input() + '0'

cnt = 0
s = ''
for i in range(1, len(a)):
    if a[i] == a[i-1]:
        cnt += 1
    else:
        s += a[i-1]
        s += str(cnt + 1)
        cnt = 0

print(len(s))
print(s)