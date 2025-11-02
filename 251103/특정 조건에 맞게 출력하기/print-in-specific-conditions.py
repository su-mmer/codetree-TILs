arr = list(map(int, input().split()))
new_arr = []

for elem in arr:
    if elem == 0:
        break
    new_arr.append(elem)

new_arr = [ x + 3 if x % 2 != 0 else x // 2 for x in new_arr ] 

for elem in new_arr:
    print(elem, end=' ')