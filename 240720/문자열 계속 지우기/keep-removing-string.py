string_a = input()
string_b = input()

i = 0
while i <= len(string_a)-len(string_b):
    if string_b == string_a[i:i+len(string_b)]:
        string_a = string_a[:i]+string_a[i+len(string_b):]
        i -= len(string_b)
    i += 1

print(string_a)