file = open("input.txt", "r")
data = [line.strip() for line in file]
rowSize = len(data[0])


def problem1():
    gamma, epsilon = '', ''
    for j in range(rowSize):
        column = get_column(j, data)
        gamma += max(column, key=column.count)
        epsilon += min(column, key=column.count)
    return int(gamma, 2) * int(epsilon, 2)


def get_column(j, data):
    column = []
    for i in range(len(data)):
        column.append(data[i][j])
    return column


def oxygen_rating(data):
    for j in range(rowSize):
        column = get_column(j, data)
        maxvalue = "1" if column.count("1") == column.count("0") else max(column, key=column.count)
        data = clearData(data, maxvalue, j)
        if len(data) == 1: break
    return int(data[0], 2)


def clearData(data, minMax, j):
    data = [elem for elem in data if elem[j] == minMax]
    return data


def CO2_rating(data):
    for j in range(rowSize):
        column = get_column(j, data)
        minvalue = "0" if column.count("1") == column.count("0") else min(column, key=column.count)
        data = clearData(data, minvalue, j)
        if len(data) == 1: break
    return int(data[0], 2)


def problem2():
    return oxygen_rating(data) * CO2_rating(data)


print("Output of the second part: ", problem1())
print("Output of the first part: ", problem2())
