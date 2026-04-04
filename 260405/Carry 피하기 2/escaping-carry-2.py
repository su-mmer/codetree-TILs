n = int(input())
numbers = [int(input()) for _ in range(n)]

def cal_carry(t_i, t_j, t_k):
    while t_i != 0 or t_j != 0 or t_k != 0:  # 각 자리수가 남았으면 
        if t_i % 10 + t_j % 10 + t_k % 10 >= 10:  # 자리수의 합이 10보다 크면
            return False  # carry 실패
        t_i, t_j, t_k = t_i // 10, t_j // 10, t_k // 10  # 다음 자리수 비교

    if carry: return True  # 모든 자리 carry 성공


max_size, sum_num = -1, -1
for i in numbers:
    for j in numbers[numbers.index(i)+1:]:
        for k in numbers[numbers.index(j)+1:]:
            carry = True

            if cal_carry(i, j, k):
                sum_num = i + j + k
            
            max_size = max(sum_num, max_size)

print(max_size)