m1, d1, m2, d2 = map(int, input().split())
a = input()
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

start = d1
for i in range(m1):
    start += month[i]

end = d2
for i in range(m2):
    end += month[i]

if week.index(a) <= (end-start) % 7:
    print((end-start) // 7 + 1)
else:
    print((end-start) // 7)