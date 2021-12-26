lines = open('input.txt').read().splitlines()


def generate_matrix(lines):
    matrix = []
    for line in lines:
        line = map(int, line)
        line = list(line)
        line.insert(0, 10)
        line.append(10)
        matrix.append(line)
    matrix.append([10] * len(matrix[0]))
    matrix.insert(0, [10] * len(matrix[0]))
    return matrix


matrixWithPadding = generate_matrix(lines)


def problem1(matrixWithPadding):
    n = len(matrixWithPadding[0])
    m = len(matrixWithPadding)
    sum = 0
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if matrixWithPadding[i][j] < matrixWithPadding[i + 1][j] and matrixWithPadding[i][j] < \
                    matrixWithPadding[i - 1][j] and \
                    matrixWithPadding[i][j] < matrixWithPadding[i][j + 1] and \
                    matrixWithPadding[i][j] < matrixWithPadding[i][j - 1]:
                sum += matrixWithPadding[i][j] + 1
    return sum


print("Output of the first part: ", problem1(matrixWithPadding))
