n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

def sequence(arr, part):
    for i in range(n1 - n2 + 1):
        if arr[i:i + n2] == part:
            return True
    return False


if sequence(arr_a, arr_b):
    print("Yes")
else:
    print("No")