n = int(input())
arr = list(map(int, input().split()))
i = 0

def find_max(value, i):
    if i == n:
        return value

    if value < arr[i]:
        return find_max(arr[i], i + 1)
    else:
        return find_max(value, i + 1)


print(find_max(0, i))