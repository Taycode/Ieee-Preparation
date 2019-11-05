num = int(input())
shoes = {}
for i in range(num):
    val = input()
    val = val.split()
    if not val[0] in shoes.keys():
        shoes[val[0]] = []
    else:
        shoes[val[0]].append(val[1])

print(shoes)