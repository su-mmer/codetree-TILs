n = int(input())
arr = list(map(int, input().split()))
arr = list(x ** 2 for x in arr)

for elem in arr:
    print(elem, end = ' ')