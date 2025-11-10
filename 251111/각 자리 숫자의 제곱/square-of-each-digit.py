n = int(input())


def sum_of(n):
    if n < 10:
        return n ** 2
    
    return sum_of(n // 10) + ((n % 10) ** 2)


print(sum_of(n))