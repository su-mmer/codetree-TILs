a, b, c = map(int, input().split())

# day, hour, minute
print((a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11))