import sys
arr = list(map(int, input().split()))

def get_score(i, j):
    return i + j


answer = sys.maxsize
sum_all = sum(arr)
for i in range(6):
    for j in range(i+1, 6):
        for m in range(i+1, 6):
            for n in range(m+1, 6):
                if j == n or j == m or m == n:
                    continue
                
                first = get_score(arr[i], arr[j])
                second = get_score(arr[m], arr[n])
                third = sum_all - first - second

                diff = max(first, second, third) - min(first, second, third)
                answer = min(diff, answer)

print(answer)