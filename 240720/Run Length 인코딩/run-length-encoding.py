string = input()
encoding = ''
ch = string[0]
ch_val = 1

for i in range(1, len(string)):
    if ch == string[i]:
        ch_val += 1
    else:
        encoding += ch
        encoding += str(ch_val)
        ch = string[i]
        ch_val = 1
encoding += ch
encoding += str(ch_val)
print(len(encoding))
print(encoding)