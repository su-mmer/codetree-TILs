a = input()
b = input()

cnt = 0
for _ in range(len(a)):
    a = a[-1] + a[:-1]
    cnt += 1
    
    if a == b:
        print(cnt)
        break
    elif cnt == len(a):
        print(-1)