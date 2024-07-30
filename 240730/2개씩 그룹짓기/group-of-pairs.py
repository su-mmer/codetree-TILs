n = int(input())
arr = list(map(int, input().split()))
answer_list = [0 for _ in range(n)]

arr.sort()

for i in range(n):
    answer_list[i] = arr[i] + arr[-i - 1]

print (max(answer_list))