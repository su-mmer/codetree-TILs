n = int(input())
arr = [input() for _ in range(n)]
ch = input()

cnt, value = 0, 0

for elem in arr:
    if elem[0] == ch:
        cnt += 1
        value += len(elem)
        
print(cnt, f'{value/cnt:.2f}')