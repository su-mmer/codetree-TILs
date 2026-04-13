import sys
arr = list(map(int, input().split()))

def get_score(i, j):
    return i + j


sum_all = sum(arr)
min_score = sys.maxsize
for a in range(5):
    for b in range(5):
        for c in range(5):
            if a == b or a == c or b == c:
                continue
            
            one = arr[a]
            two = get_score(arr[b], arr[c])
            three = sum_all - one - two
            
            if one == two or two == three or one == three:
                continue
            
            score = max(one, two, three) - min(one, two, three)
            min_score = min(score, min_score)

print(min_score) if min_score != sys.maxsize else print(-1)