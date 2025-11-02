arr = list(map(int, input().split()))
num_list = [0] * 11

for elem in arr:
    if elem == 0:
        break
    num_list[elem//10] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {num_list[i]}")