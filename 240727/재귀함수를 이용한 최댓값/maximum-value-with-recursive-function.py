n = int(input())
arr = list(map(int, input().split()))
i = 0

def find_max(i):
    if i == 0:
        return arr[i]

    return max(find_max(arr[i-1]), arr[i])


print(find_max(arr[n - 1]))