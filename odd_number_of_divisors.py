their_input = input()
a = int(their_input.split()[0])
b = int(their_input.split()[1])

num_dict = {}


def get_divisors(num):
    num_divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            num_divisors.append(i)
    return num_divisors


def get_num_in_interval(first_num, second_num):
    num_list = []
    for i in range(first_num, second_num + 1):
        num_list.append(i)
    return num_list


def check_if_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def main(first_num, second_num):
    num_list = get_num_in_interval(first_num, second_num)
    for i in num_list:
        i_divisors = get_divisors(i)
        num_dict[i] = len(i_divisors)
    odd_numbers = list(filter(check_if_odd, num_dict.values()))
    print(len(odd_numbers))


if __name__ == "__main__":
    main(a, b)
