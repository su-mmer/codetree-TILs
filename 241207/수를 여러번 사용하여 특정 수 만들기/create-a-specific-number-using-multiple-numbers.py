a, b, c = map(int, input().split())

sum_ab = 0  # a와 b를 더한 값
sum_max = 0  # 최대값
i = 0  # a 더할 횟수 0 ~
while(i * a <= c):
    sum_ab = i * a
    while(sum_ab + b <= c):  # b를 더한 값이 c보다 이하일때까지만
        sum_ab += b
    sum_max = max(sum_max, sum_ab)
    i += 1
    
print(sum_max)