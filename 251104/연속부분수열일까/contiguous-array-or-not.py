a_num, b_num = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

flag = False  # 연속 부분 수열 판단
for i in range(len(a_list)):
    if a_list[i] == b_list[0]:  # a의 원소와 b 리스트의 첫 번째 원소가 같다면
        for j in range(1, len(b_list)):  # b 리스트가 연속 부분 수열인지 판단
            if a_list[i+j] != b_list[j]:  # 원소가 서로 다르면 중단하고 넘어감
                break
            flag = True  # b의 원소가 전부 일치하면 True로 변경
        if flag == True:  # 전체 반복문 종료
            print("Yes")
            break

if flag == False:
    print("No")