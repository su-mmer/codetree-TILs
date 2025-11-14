n = int(input())
questions = [ list(map(int, input().split())) for _ in range(n) ]
arr = [ 0 for _ in range(201) ]

for q in questions:
    if q[0] < 0 and q[1] > 0:
        for i in range(q[1]):
            arr[i] += 1
        for i in range(101, abs(q[0])+100+1):
            arr[i] += 1
    elif q[0] < 0 and q[1] < 0:
        for i in range(102, abs(q[0])+100+1):
            arr[i] += 1
    else:
        for i in range(q[0], q[1]):
            arr[i] += 1

print(max(arr))