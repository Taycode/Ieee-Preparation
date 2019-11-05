their_input = input().split()
array_list = input().split(" ")
array_list = list(map(int, array_list))

second_array_list = input().split(" ")

second_array_list = list(map(int, second_array_list))

second_array_list.sort()


m, n = len(array_list), len(second_array_list)
i, j = 0, 0
res = []

while i < m and j < n:
    if array_list[i] < second_array_list[j]:
        res.append(array_list[i])
        i += 1
    else:

        res.append(second_array_list[j])

        j += 1

response = res + array_list[i:] + second_array_list[j:]

response = map(str, response)

print(' '.join(response))
