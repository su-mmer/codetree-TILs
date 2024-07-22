n = int(input())
arr = list(map(int, input().split()))

def absolute(myarr):
    for i in range(n):
        if myarr[i] < 0:
            myarr[i] = -myarr[i]

absolute(arr)
for elem in arr:
    print(elem, end=' ')