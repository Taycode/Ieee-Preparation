their_input = input().split()
crissy = int(their_input[0])
jace = int(their_input[1])
word = crissy + jace
if jace and crissy:
    my_min = min(jace, crissy)
    if my_min >= word // 3:
        res = word // 3
        print(res)
    else:
        print(my_min)
else:
    print(0)
