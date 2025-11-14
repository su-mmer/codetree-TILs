n, k = map(int, input().split())
quest = [ list(map(int, input().split())) for _ in range(k) ]
arr = [ 0 for _ in range(n+1) ]

for q in quest:
    for i in range(q[0], q[1]+1):
        arr[i] += 1

print(max(arr))