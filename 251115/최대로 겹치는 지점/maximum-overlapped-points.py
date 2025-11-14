n = int(input())
questions = [ list(map(int, input().split())) for _ in range(n)]
arr = [ 0 for _ in range(101)]

for q in questions:
    for i in range(q[0], q[1]+1):
        arr[i] += 1

print(max(arr))