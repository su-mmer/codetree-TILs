n, q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    q_list = list(map(int, input().split()))
    if q_list[0] == 1:
        print(arr[q_list[1]-1])
    elif q_list[0] == 2:
        if q_list[1] not in arr:
            print(0)
        elif arr.count(q_list[1]) == 1:
            print(arr.index(q_list[1]) + 1)
        else:
            print(arr.index(q_list[1]) + 1)
    else:
        for j in arr[q_list[1]-1:q_list[2]]:
            print(j, end=' ')
        print()