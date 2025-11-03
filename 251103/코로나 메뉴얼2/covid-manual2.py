cnt_list = [0] * 4

for i in range(3):
    status, temperature = input().split()
    temperature = int(temperature)

    if temperature >= 37:
        if status == 'Y':
            cnt_list[0] += 1  # A
        elif status == 'N':
            cnt_list[1] += 1  # B
    elif temperature < 37:
        if status == 'Y':
            cnt_list[2] += 1  # C
        elif status == 'N':
            cnt_list[3] += 1  # D

for elem in cnt_list:
    print(elem, end=' ')

if cnt_list[0] >= 2:
    print("E")