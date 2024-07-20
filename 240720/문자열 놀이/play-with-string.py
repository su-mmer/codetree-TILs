s, q = tuple(input().split())
mystr = list(s)

for _ in range(int(q)):
    question, a, b = tuple(input().split())
    if question == "1":
        a, b = int(a), int(b)
        mystr[a-1], mystr[b-1] = mystr[b-1], mystr[a-1]
        print(''.join(mystr))
    else:
        temp_string = ''.join(mystr)
        print(temp_string.replace(a, b))
        mystr = list(temp_string.replace(a, b))