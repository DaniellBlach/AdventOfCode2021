import os.path

file = open("input.txt", "r")
measurements = [int(line.strip()) for line in file]


def problem1():
    counter = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            counter += 1
    return counter;


def problem2():
    counter = 0
    for i in range(len(measurements) - 2):
        if sum(measurements[i:i + 3]) < sum(measurements[i + 1:i + 4]):
            counter += 1
    return counter


print("Output of the first part: ",problem1())
print("Output of the second part: ",problem2())
