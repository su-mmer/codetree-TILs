s, q = tuple(input().split())
s = list(s)

for _ in range(int(q)):
    question, s_1, s_2 = input().split()

    if question == "1":
        s_1, s_2 = int(s_1)-1, int(s_2)-1
        s[s_1], s[s_2] = s[s_2], s[s_1]
    else:
        for i, char in enumerate(s):
            if char == s_1:
                s[i] = s_2
    
    print(''.join(s))