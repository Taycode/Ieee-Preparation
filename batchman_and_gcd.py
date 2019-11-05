from math import gcd

_ = input()

data = [int(a) for a in input().split(" ")]
second_data = data.copy()
length = len(data)

count = 0

res = []

length_of_second_data = len(second_data)

i = 0
j = 0

while i < length and j < length_of_second_data:

    res.append(gcd(data[i], second_data[j]))

    j += 1

    if j == length_of_second_data:
        j = 0
        i += 1

print(len(set(res)))