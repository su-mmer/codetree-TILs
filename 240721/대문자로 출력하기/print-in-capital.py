string = input()
arr = list(string)
upper_arr = []

for ch in arr:
    if ch.isalpha():
        upper_arr.append(ch.upper())

print(''.join(upper_arr))