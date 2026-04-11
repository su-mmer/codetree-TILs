n, k = map(int, input().split())
numbers = [0] * (10000 + 1)

# 입력받는 G, H에 따라 배열에 점수 입력
for _ in range(n):
    num, alphabet = input().split()
    numbers[int(num)] = 1 if alphabet == 'G' else 2

max_score = 0
for i in range(1, 10000 - k + 1):
    score = 0
    for j in range(i, i + k + 1):
        score += numbers[j]

    max_score = max(score, max_score)

print(max_score)