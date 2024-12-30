# x, y 축 직선을 1개씩 그어 균형 있게 나눈다 (항상 짝수)
# 가장 많은 점이 있는 구역의 점의 개수 M의 최소값
n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]

min_m = 101
for x in range(2, 101, 2):
    for y in range(2, 101, 2):
        m = 0
        one, two, three, four = 0, 0, 0, 0
        for a, b in arr:
            if a < x and b > y:
                one += 1
            elif a < x and b < y:
                two += 1
            elif x < a and b > y:
                three += 1
            elif x < a and b < y:
                four += 1
        m = max(one, two, three, four)
        min_m = min(min_m, m)

print(min_m)