def is_my_answer(n):
    return (n // 10 + n % 10) % 5 == 0 and n % 2 == 0


n = int(input())
print("Yes" if is_my_answer(n) else "No")