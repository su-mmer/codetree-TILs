a, b = map(int, input().split())
modular_list = [0] * 10

while a > 1:
    modular_list[a % b] += 1
    a //= b

sum_val = 0
for elem in modular_list:
    sum_val += elem ** 2

print(sum_val)