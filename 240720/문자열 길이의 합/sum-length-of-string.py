n = int(input())
arr = [input() for _ in range(n)]
value, a_value = 0, 0

for string in arr:
    value += len(string)
    if string[0] == 'a':
        a_value += 1

print(value, a_value)