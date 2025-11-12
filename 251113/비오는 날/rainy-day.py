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

pv = Data("9999-99-99", "Mon", "Rain")
for i, d in enumerate(dates):
    if d.weather == "Rain" and pv.date > d.date:
        pv = d

print(pv.date, pv.day, pv.weather, sep=' ')