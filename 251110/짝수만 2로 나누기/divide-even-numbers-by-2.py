def divide_even(even_list, n):
    for i, elem in enumerate(even_list):
        if elem % 2 == 0:
            even_list[i] = elem // 2
    return even_list


n = int(input())
arr = list(map(int, input().split()))

for elem in divide_even(arr, n):
    print(elem, end=' ')