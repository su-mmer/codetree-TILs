class Data:
    def __init__ (self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())

dates = []
for _ in range(n):
    date, day, weather = input().split()
    dates.append(Data(date, day, weather))

for i, d in enumerate(dates):
    if d.weather == "Rain":
        print(d.date, d.day, d.weather, sep=' ')
        break