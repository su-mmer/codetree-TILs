n = int(input())
arr = [0 for _ in range(100001)]
point = 0

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == "L":
        for i in range(point-a, point):
            arr[i] = "white"
        point -= a
    elif b == "R":
        for i in range(point, point+a):
            arr[i] = "black"
        point += a


print(arr.count("white"), arr.count("black"))