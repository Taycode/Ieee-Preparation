def main(n, a, b):
    my_list = [b] * (n//b + 1)
    remainder = sum(my_list) - n
    while remainder != 0:
        while remainder > b-a:
            my_list[len(my_list)-1] -= b-a
            remainder -= b - a
            my_list.sort()
        else:
            my_list[len(my_list) - 1] -= remainder
            my_list.sort()

        return my_list


def if_possible(n, a, b):
    if (n - a) >= a:
        valid_response = main(n, a, b)
        print("YES")
        valid_response = list(map(str, valid_response))
        print(' '.join(valid_response))
    else:
        print("NO")


their_input = input().split()
n = int(their_input[0])
a = int(their_input[1])
b = int(their_input[2])

if_possible(n, a, b)
