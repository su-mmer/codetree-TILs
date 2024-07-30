n = int(input())
arr = list(map(int, input().split()))

for i in range(0, n, 2):
    print(sorted(arr[:i+1])[i//2], end=' ')