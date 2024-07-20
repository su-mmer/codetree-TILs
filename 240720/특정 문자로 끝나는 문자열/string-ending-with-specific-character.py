arr = [input() for _ in range(10)]
ch = input()
flag = False

for elem in arr:
    if elem[-1] == ch:
        print(elem)
        flag = True

if flag == False:
    print("None")