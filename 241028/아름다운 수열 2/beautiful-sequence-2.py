n, m = map(int, (input().split()))
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

# B의 원소의 순서를 바꾸는 게 아름다운 수열
replace = [0]*10
for i in arr_b:
    replace[i] += 1

cnt = 0
for i in range(n-m+1):
    flag = False
    if arr_a[i] in arr_b:
        copy = replace[:]
        flag = True
        for j in range(m):
            if arr_a[i+j] in arr_b:
                copy[arr_a[i+j]] -= 1
        for k in copy:
            if k != 0:
                flag = False
    if flag == True:
        cnt += 1

print(cnt)