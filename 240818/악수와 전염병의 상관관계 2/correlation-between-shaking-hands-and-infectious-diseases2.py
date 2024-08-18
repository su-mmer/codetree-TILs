N, K, P, T = map(int, input().split())  # n명, k번의 악수, 처음 걸린 p, 총 악수 t번
arr_n = [0 for _ in range(101)]  # 개발자 번호
arr_t = [[0 for _ in range(3)] for _ in range(251)]  # 악수 list
arr_k = [0 for _ in range(101)]  # 감염 횟수 몇 번 남았니

# 악수한 시간이 랜덤으로 들어오므로 저장하기 위한 list 생성
for i in range(T):
    arr_t[i][0], arr_t[i][1], arr_t[i][2] = map(int, input().split())
# 악수한 시간 오름차순 sort
arr_t.sort()

# 첫 번째 감염자
arr_n[P] = 1
# 감염 기록
for elem in arr_t:
    if elem[0] != 0:
        _, x, y = elem[0], elem[1], elem[2]  # n초, x개발자, y개발자
        if arr_n[x] == 1 or arr_n[y] == 1:  # 감염자가 있으면
            # 감염자끼리 악수 해도 횟수를 차감해야 하므로 if 2번
            if arr_k[x] < K:  # x개발자 감염 횟수 남음
                arr_n[y] = 1  # y 감염시킴
                arr_k[x] += 1  # x의 감염 횟수 차감
            if arr_k[y] < K:  # y개발자 감염 횟수 남음
                arr_n[x] = 1  # x 감염시킴
                arr_k[y] += 1  # y 감염 횟수 차감

for elem in arr_n[1:N+1]:
    print(elem, end='')