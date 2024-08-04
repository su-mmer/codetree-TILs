n = int(input())
arr = [0 for _ in range(1001)]
point = 0

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == "L":
        for i in range(point - a, point):
            arr[i] += 1
        point -= a
    elif b == "R":
        for i in range(point, point + a):
            arr[i] += 1
        point += a
        
value = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        value += 1

print(value)