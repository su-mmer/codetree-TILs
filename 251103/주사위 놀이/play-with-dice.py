arr = list(map(int, input().split()))
num_list = [0]*7

for i in arr:
    num_list[i] += 1

for i in range(1, 7):
    print(f"{i} - {num_list[i]}")