n = int(input())
questions = [ list(map(int, input().split())) for _ in range(n) ]
arr = [ 0 for _ in range(201) ]

for q in questions:
    if q[0] < 0:
        q[0] = -1 * q[0] + 100
        q[1] += 100

    for i in range(q[0], q[1]):
        arr[i] += 1

print(max(arr))