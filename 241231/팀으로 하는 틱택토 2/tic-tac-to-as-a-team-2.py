arr = [ list(input()) for _ in range(3) ]

cnt = 0

def count_set(aset):
    if len(set(aset)) == 2:
        return 1
    else:
        return 0
    # return 1 if len(set(aset)) == 2 else 0


# 가로
for column in arr:
    cnt += count_set(column)

# 세로
li_a, li_b, li_c = [], [], []
for row in arr:
    li_a.append(row[0])
    li_b.append(row[1])
    li_c.append(row[2])
cnt += count_set(li_a)
cnt += count_set(li_b)
cnt += count_set(li_c)

# 대각선
cnt += count_set([arr[0][0], arr[1][1], arr[2][2]])
cnt += count_set([arr[0][2], arr[1][1], arr[2][0]])
print(cnt)