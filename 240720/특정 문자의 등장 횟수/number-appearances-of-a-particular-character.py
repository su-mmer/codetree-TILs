arr = input()
ee_cnt, eb_cnt = 0, 0

for i in range(len(arr)-1):
    if "ee" == arr[i:i+2]:
        ee_cnt += 1
    elif "eb" == arr[i:i+2]:
        eb_cnt += 1

print(ee_cnt, eb_cnt)