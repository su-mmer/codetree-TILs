string = input()

sum_val = 0
for c in string:
    if c.isdigit():
        sum_val += int(c)

print(sum_val)