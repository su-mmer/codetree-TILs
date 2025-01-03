n = int(input())
arr = list(map(int, input().split()))

ans = []
for i in range(1, n + 1):
    init = i  # 수열의 첫 번째 값
    ans.append(init)

    for j in range(n - 1):  # 원소의 합을 돌면서 원소 추측
        next_var = arr[j] - init  # 다음 값 추측

        flag = False
        if next_var > 0:  # next_var가 0보다 큰 경우에만
            flag = True
            for k in ans:  # 처음 나오는 값인지 찾기
                if next_var == k:
                    flag = False
                    break

        if flag == True:  # 처음 나오는 값이면 추가
            ans.append(next_var)
            init = next_var
        else:  # 이미 있는 값이면 초기화시키고 넘어감
            ans = []
            break

    if len(ans) == n:  # 수열 다 채웠으면 출력
        for elem in ans:
            print(elem, end=' ')
        break