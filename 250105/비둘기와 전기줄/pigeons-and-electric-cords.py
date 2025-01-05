n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]
peace = [0] * 11
where = [False] * 11

cnt = 0
for p, w in arr:
    if not where[p]:  # 초면 비둘기
        where[p] = True
        peace[p] = w
    elif where[p] and peace[p] != w:  # 방향이 바뀐 구면 비둘기
        peace[p] = w
        cnt += 1

print(cnt)