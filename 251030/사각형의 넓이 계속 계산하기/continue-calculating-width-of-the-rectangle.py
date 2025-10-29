while True:
    w, h, c = input().split()
    w, h = int(w), int(h)
    print(w * h)
    if c == "C":
        break