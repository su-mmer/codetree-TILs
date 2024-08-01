a, b, c = map(int, input().split())

def datetime(a, b, c):
    if a == 11:
        if b < 11 or (b == 11 and c < 11):
            return -1
            
    return (a - 11) * 24 * 60 + (b - 11) * 60 + c - 11

print(datetime(a, b, c))