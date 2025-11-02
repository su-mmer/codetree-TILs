n = int(input())

count = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    if sum(arr) / 4 >= 60:
        print("pass")
        count += 1
    else:
        print("fail")

print(count)