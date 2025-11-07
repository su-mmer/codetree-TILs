string = input()

ee_num, eb_num = 0, 0
for i in range(len(string)-1):
    if string[i:i+2] == 'ee':
        ee_num += 1
    if string[i:i+2] == 'eb':
        eb_num += 1

print(ee_num, eb_num)