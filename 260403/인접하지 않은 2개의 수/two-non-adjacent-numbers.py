n = int(input())
numbers = list(map(int, input().split()))

max_answer = 0
for i in range(n-2):
    for j in range(i+2, n):
        answer = numbers[i] + numbers[j]

        max_answer = max(max_answer, answer)

print(max_answer)