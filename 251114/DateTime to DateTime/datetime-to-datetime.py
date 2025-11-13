a, b, c = map(int, input().split())

time = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)
print(-1) if time < 0 else print(time)