n = int(input())
price = list(map(int, input().split()))

profit = 0  # 이익
for i in range(n-1):
    for j in range(i+1, n):
        if price[i] < price[j] and profit < (price[j] - price[i]):  # 오른쪽의 값이 더 크고 이익이 더 크다면
            profit = price[j] - price[i]

print(profit)