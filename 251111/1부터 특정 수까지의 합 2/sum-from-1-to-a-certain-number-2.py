n = int(input())


def sum_of_all(n):
    if n == 1:
        return 1

    return sum_of_all(n-1) + n

    
print(sum_of_all(n))