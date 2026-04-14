n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            flag = False
            # first
            if (i + a1 >= n and abs(abs(i - a1) - n) <= 2) or abs(i - a1) <= 2:
                if (j + b1 >= n and abs(abs(j - b1) - n) <= 2) or abs(j - b1) <= 2:
                    if (k + c1 >= n and abs(abs(k - c1) - n) <= 2) or abs(k - c1) <= 2:
                        cnt += 1
                        flag = True
            # second
            if (i + a2 >= n and abs(abs(i - a2) - n) <= 2) or abs(i - a2) <= 2:
                if (j + b2 >= n and abs(abs(j - b2) - n) <= 2) or abs(j - b2) <= 2:
                    if (k + c2 >= n and abs(abs(k - c2) - n) <= 2) or abs(k - c2) <= 2:
                        if flag: continue  # 중복처리
                        cnt += 1
                                                
print(cnt)