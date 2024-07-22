n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

def plus(a1, a2):
    global arr
    total = 0
    for elem in arr[a1:a2 + 1]:
        total += elem
    return total

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(plus(a1, a2))