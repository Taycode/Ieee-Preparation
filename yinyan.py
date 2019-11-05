import random
my_input = int(input())
rand_num = random.randint(0, my_input)

if my_input % 2 == 0:
    print("y" * int(my_input / 2 + 1) + "Y" * int(my_input / 2 - 1))

else:
    print("y" * rand_num + "Y" * (my_input - rand_num))


