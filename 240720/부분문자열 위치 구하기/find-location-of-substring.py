string = input()
find_str = input()

if find_str in string:
    print(string.index(find_str))
else:
    print(-1)