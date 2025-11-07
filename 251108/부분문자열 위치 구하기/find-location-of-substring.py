input_str = input()
target_str = input()

for i in range(len(input_str)-len(target_str)+1):
    if input_str[i:i+len(target_str)] == target_str:
        print(i)
        break

if target_str not in input_str:
    print(-1)

# print(input_str.find(target_str))