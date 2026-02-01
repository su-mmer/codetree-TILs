def cal_sum(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
sum = 0
a, b = map(int, input().split())
for i in range(a, b+1):
    if cal_sum(i):
        sum += i

print(sum)