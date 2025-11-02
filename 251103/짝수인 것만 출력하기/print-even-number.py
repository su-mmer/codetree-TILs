n = int(input())
arr = list(map(int, input().split()))
even = [x for x in arr if x % 2 == 0]

for elem in even:
    print(elem, end=' ')