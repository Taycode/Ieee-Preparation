def get_data_and_convert_to_matrix(rows, columns):
    data = []
    for i in range(rows):
        row_data = list(input().split())
        for j in range(columns):
            row_data[j] = int(row_data[j])

        data.append(row_data)
    return data


def flip_first_column(matrix):
    for a in range(len(matrix)):
        if matrix[a][0] == 0:
            matrix[a][0] = 1
        elif matrix[a][0] == 1:
            matrix[a][0] = 0

    return matrix


def flip_row(row):
    for a in range(len(row)):
        if row[a] == 0:
            row[a] = 1
        elif row[a] == 1:
            row[a] = 0


def convert_to_decimal(row):
    num = 0
    for a in row:
        power = len(row) - row.index(a) - 1
        num += a * 2 ** power
    return num


def main():
    num = 0
    their_input = input().split()
    rows = int(their_input[0])
    columns = int(their_input[1])
    data = get_data_and_convert_to_matrix(rows, columns)
    data = flip_first_column(data)
    for a in range(1):
        flip_row(data[a])

    for a in data:
        num += convert_to_decimal(a)

    print(data)
    print(num)


if __name__ == "__main__":
    main()
