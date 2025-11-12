n, k, t = input().split()
n, k = int(n), int(k)
arr = [ input() for _ in range(n) ]
arr_t = []

for elem in arr:
    if t == elem[:len(t)]:
        arr_t.append(elem)

arr_t.sort()
print(arr_t[k-1])