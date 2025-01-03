n = 15
arr = list(map(int, input().split()))
arr.sort()

for a in arr:
    for b in arr[arr.index(a)+1:]:
        for c in arr[arr.index(b)+1:]:
            for d in arr[arr.index(c)+1:]:
                if (a + b) not in arr:
                    continue
                if (b + c) not in arr:
                    continue
                if (c + d) not in arr:
                    continue
                if (d + a) not in arr:
                    continue
                if (a + b + c) not in arr:
                    continue
                if (a + b + d) not in arr:
                    continue
                if (a + c + d) not in arr:
                    continue
                if (b + c + d) not in arr:
                    continue
                if (a + b + c + d) not in arr:
                    continue
                A, B, C, D = a, b, c, d
print(A, B, C, D)