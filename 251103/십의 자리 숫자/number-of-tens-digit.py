arr = list(map(int, input().split()))
num_list = [0] * 10

for elem in arr:
    if elem == 0:
        break
    num_list[elem // 10] += 1

for i in range(1, 10):
    print(f"{i} - {num_list[i]}")