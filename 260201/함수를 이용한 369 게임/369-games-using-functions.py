def find_3_6_9 (n):
    n = str(n)
    for i in n:
        if i == "3" or i == "6" or i == "9":
            return True
    return False

def check_num(a, b):
    sum = 0
    for i in range(a, b+1):
        if find_3_6_9(i) or i % 3 == 0:
            sum += 1
    return sum

a, b = map(int, input().split())
print(check_num(a, b))