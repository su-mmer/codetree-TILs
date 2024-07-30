n, k, T = input().split()
arr = [input() for _ in range(int(n))]

cnt = 0
for elem in sorted(arr):
    if elem[:len(T)] == T:
        cnt += 1
        if cnt == int(k):
            print(elem)