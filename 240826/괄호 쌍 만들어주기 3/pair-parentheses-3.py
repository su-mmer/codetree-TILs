# 괄호의 쌍을 이룰 수 있는 서로 다른 가지수
string = input()

num = 0
for i in range(len(string)):
    if string[i] == "(":
        for j in range(i+1, len(string)):
            if string[j] == ")":
                num += 1

print(num)