arr = int(input())
arr = list(map(int, input().split()))
length = len(arr)

answer = 0
for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            if arr[i] <= arr[j] and arr[j] <= arr[k]:
                answer += 1

print(answer)