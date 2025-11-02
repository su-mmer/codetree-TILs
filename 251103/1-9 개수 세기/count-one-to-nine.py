n = int(input())
arr = list(map(int, input().split()))
num_list = [0] * 10

for i in arr:
    num_list[i] += 1

for elem in num_list[1:]:
    print(elem)