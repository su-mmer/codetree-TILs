a_list = [ list(map(int, input().split())) for _ in range(3) ]
space = input()
b_list = [ list(map(int, input().split())) for _ in range(3) ]
 
for i in range(3):
    for j in range(3):
        print(a_list[i][j] * b_list[i][j], end=' ')
    print()