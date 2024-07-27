n = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

if sorted(arr_a) == sorted(arr_b):
    print("Yes")
else:
    print("No")