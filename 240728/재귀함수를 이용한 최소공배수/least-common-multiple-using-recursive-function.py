n = int(input())
arr = list(map(int, input().split()))

def lcm(a, b):
    for num in range(max(a, b), a * b + 1):
       if num % a == 0 and num % b == 0:
            return num 


# f(n) = lowest..?(f(n-1), arr[n])
# End: arr[0]
def calculate(n, value):
    if n == 0:
        return lcm(arr[0], value)

    return calculate(n - 1, lcm(arr[n], value))


print(calculate(n - 1, 1))