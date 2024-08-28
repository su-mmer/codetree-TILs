string = input()

num = 0
for i in range(1, len(string)):
    if string[i] == '(' and string[i-1] == '(':
        for j in range(i+2, len(string)):
            if string[j] == ")" and string[j-1] == ")":
                num += 1

print(num)