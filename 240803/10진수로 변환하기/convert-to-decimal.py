binary = input()
answer = 0

for i in range(len(binary)):
    answer = answer * 2 + int(binary[i])

print(answer)