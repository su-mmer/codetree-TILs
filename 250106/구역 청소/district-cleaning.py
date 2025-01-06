xa, xb = map(int, input().split())
xc, xd = map(int, input().split())

if xb <= xc or xd <= xa:
  print(xb - xa + xd - xc)
elif xb <= xd:
  print(xd - xa)
else:
  print(xb - xc)