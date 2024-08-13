n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

index = []
for i in range(n):
    if i == 0 or arr[i-1] != arr[i]:
        index.append(i)

# print(index)
max_count = 0
if len(index) == 1:
    max_count = n

for i in range(1, len(index)):
    if index[i] - index[i-1] > max_count:
        max_count = index[i] - index[i-1]

print(max_count)