str1 = input()
str2 = input()
str3 = input()
str1_len = len(str1)
str2_len = len(str2)
str3_len = len(str3)
max = str1_len
min = str1_len

if max < str2_len:
    max = str2_len
if max < str3_len:
    max = str3_len
if str2_len < min:
    min = str2_len
if str3_len < min:
    min = str3_len

print(max-min)