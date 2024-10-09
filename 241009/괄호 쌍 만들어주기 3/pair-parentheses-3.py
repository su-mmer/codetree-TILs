arr = input()
length = len(arr)

answer = 0
for i in range(length):
    for j in range(i + 1, length):
        if arr[i] == '(' and arr[j] == ')':
            answer += 1

print(answer)