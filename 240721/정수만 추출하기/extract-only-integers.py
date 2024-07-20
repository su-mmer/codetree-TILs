str1, str2 = input().split()
extract1, extract2 = '', ''

for ch in str1:
    if ch.isdigit():
        extract1 += ch
    else:
        break
for ch in str2:
    if ch.isdigit():
        extract2 += ch
    else:
        break
print(int(extract1) + int(extract2))