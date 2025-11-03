n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    q_list = list(map(int, input().split()))

    if q_list[0] == 1:
        a = q_list[1]
        print(arr[a-1])

    elif q_list[0] == 2:
        b = q_list[1]
        if b not in arr:
            print(0)
        elif arr.count(q_list[1]) == 1:
            print(arr.index(q_list[1]) + 1)
        else:
            print(arr.index(q_list[1]) + 1)

    else:
        for j in arr[q_list[1]-1:q_list[2]]:
            print(j, end=' ')
        print()