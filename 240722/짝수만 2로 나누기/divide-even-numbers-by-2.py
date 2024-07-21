n = int(input())
arr = list(map(int, input().split()))

def even_divide(myarr):
    for i in range(len(myarr)):
        if myarr[i] % 2 == 0:
            myarr[i] = int(myarr[i] / 2)
    return myarr

for elem in even_divide(arr[:]):
    print(elem, end = ' ')