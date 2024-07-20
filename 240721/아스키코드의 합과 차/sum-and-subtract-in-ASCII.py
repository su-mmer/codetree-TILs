ch1, ch2 = input().split()
ch1, ch2 = ord(ch1), ord(ch2)

if ch1 < ch2:
    sub = ch2 - ch1
else:
    sub = ch1 - ch2
print(ch1 + ch2, sub)