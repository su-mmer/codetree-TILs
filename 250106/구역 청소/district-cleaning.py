xa, xb = map(int, input().split())
xc, xd = map(int, input().split())

arround = (xb - xa + xd - xc) if xb < xc or xd < xa else xb - xa + xd - xc - (xd - xa)
print(arround)