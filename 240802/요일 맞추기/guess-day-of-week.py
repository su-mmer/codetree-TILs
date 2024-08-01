m1, d1, m2, d2 = map(int, input().split())

day_of_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day = ((sum(day_of_year[1:m2]) + d2) - (sum(day_of_year[1:m1]) + d1)) % 7
if day < 0: day = -day
print(weeks[day])