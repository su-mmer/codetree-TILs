n = int(input())
arr = list(map(int, input().split()))

# arr 쪼개기
def merge_sort(array, low, high):
    global arr
    if low < high:  # 원소가 2개 이상
        mid = (low + high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)

merged_arr = [[] for _ in range(n)]

def merge(array, low, mid, high):
    global arr
    i = low
    j = mid + 1

    k = low
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            merged_arr[k] = array[i]
            i += 1
        else:
            merged_arr[k] = array[j]
            j += 1
        k += 1

    while i <= mid:
        merged_arr[k] = array[i]
        k += 1
        i += 1
    
    while j <= high:
        merged_arr[k] = array[j]
        k += 1
        j += 1
    
    for elem in range(low, high + 1):
        arr[elem] = merged_arr[elem]

merge_sort(arr, 0, n - 1)

for i in arr:
    print(i, end=' ')