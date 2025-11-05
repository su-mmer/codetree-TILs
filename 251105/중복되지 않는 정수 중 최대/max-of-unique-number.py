n = int(input())
nums = list(map(int, input().split()))
re = [0] * 1001

# Please write your code here.
for elem in nums:
    re[elem] += 1

max_val = -1
for i, elem in enumerate(re):
    if elem == 1 and max_val < i:
        max_val = i

print(max_val)