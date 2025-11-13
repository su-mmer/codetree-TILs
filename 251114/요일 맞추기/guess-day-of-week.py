m1, d1, m2, d2 = map(int, input().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

start = d1
for i in range(m1):
    start += month[i]

end = d2
for i in range(m2):
    end += month[i]

print(week[(end-start) % 7])