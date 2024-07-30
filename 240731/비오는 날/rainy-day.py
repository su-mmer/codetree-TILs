class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather 


n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
days = [Weather(date, day, weather) for date, day, weather in arr]

end="9999-99-99"
for i in range(n):
    if days[i].weather == "Rain" and days[i].date < end:
        end = days[i].date
        index = i

print(f"{days[index].date} {days[index].day} {days[index].weather}")