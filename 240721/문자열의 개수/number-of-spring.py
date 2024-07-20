arr = []

while True:
    string = input()
    if string == "0":
        break
    else:
        arr.append(string)

print(len(arr))
for elem in arr[::2]:
    print(elem)