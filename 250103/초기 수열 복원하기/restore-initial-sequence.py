n = int(input())
arr = list(map(int, input().split()))

ans = ''  # 초기 수열
for i in range(1, n + 1):
    init = i  # 수열의 첫 번째 값
    ans += str(init)  # find를 쓰기 위해 str로 변경...
    for j in range(n - 1):  # 원소의 합을 돌면서 원소 추측
        next_var = arr[j] - init  # 다음 값 추측
        if ans.find(str(next_var)) == -1 and next_var > 0:  # 처음 나오는 값이면 수열에 추가
            ans += str(next_var)
            init = next_var
        else:  # 이미 있는 값이면 초기화시키고 넘어감
            ans = ''
            break
    if len(ans) == n:  # 수열 다 채웠으면 출력
        for elem in ans:
            print(int(elem), end=' ')
        break