n = int(input())
arr = [-1]
for _ in range(n):
    arr.append(int(input()))

count = 0
for i in range(n):
    if arr[i] == -1 or arr[i-1] != arr[i]:
        count += 1
        
print(count)