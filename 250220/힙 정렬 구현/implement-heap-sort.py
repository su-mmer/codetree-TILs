num = int(input())
array = list(map(int, input().split()))

def heapify(parent, arr, n):
    largest = parent
    l = parent * 2 + 1
    r = parent * 2 + 2
    # print(largest, l, r)

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != parent:
        arr[largest], arr[parent] = arr[parent], arr[largest]
        heapify(largest, arr, n)

def heap_sort(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(i, arr, n)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(0, arr, i)

heap_sort(array, num)

for enum in array:
    print(enum, end=' ')