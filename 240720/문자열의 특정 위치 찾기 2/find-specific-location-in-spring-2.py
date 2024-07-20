apple = "apple"
banana = "banana"
grape = "grape"
bluebery = "blueberry"
orange = "orange"

cnt = 0
ch = input()
if apple[2] == ch or apple[3] == ch:
    print(apple)
    cnt += 1
if banana[2] == ch or banana[3] == ch:
    print(banana)
    cnt += 1
if grape[2] == ch or grape[3] == ch:
    print(grape)
    cnt += 1
if bluebery[2] == ch or bluebery[3] == ch:
    print(bluebery)
    cnt += 1
if orange[2] == ch or orange[3] == ch:
    print(orange)
    cnt += 1
print(cnt)