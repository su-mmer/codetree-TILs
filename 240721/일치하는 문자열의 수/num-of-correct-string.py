n, A = input().split()
cnt = 0

for num in range(int(n)):
    string = input()
    if string == A:
        cnt += 1

print(cnt)