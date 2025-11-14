n = int(input())
questions = [ list(input().split()) for _ in range(n) ]
arr = [ 0 for _ in range(2002) ]
OFFSET=1000

pv = OFFSET
for q in questions:
    q[0] = int(q[0])

    if q[1] == "L":
        for i in range(pv, pv-q[0], -1):
            arr[i] += 1
        pv = pv - q[0]
    elif q[1] == "R":
        for i in range(pv, pv+q[0]):
            arr[i] += 1
        pv = pv + q[0]
    # print(pv)

cnt = 0
for i in arr:
    if i >= 2:
        cnt += 1
    
print(cnt)