arr, ch = tuple(input().split())
if arr.find(ch) == -1:
    print("No")
else:
    print(arr.find(ch))