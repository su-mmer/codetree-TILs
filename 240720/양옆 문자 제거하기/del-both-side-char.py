string = input()
arr = list(string)

arr.pop(1)
arr.pop(-2)
print(''.join(arr))