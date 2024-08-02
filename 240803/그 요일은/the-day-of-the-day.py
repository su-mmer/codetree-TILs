m1, d1, m2, d2 = map(int, input().split())
day = input()

days_of_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

between = sum(days_of_year[1:m2]) - sum(days_of_year[1:m1]) + d2 - d1 + 1

print(between // 7 + 1) if weeks.index(day) <= between % 7 else print(between // 7)