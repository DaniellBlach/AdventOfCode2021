file = open("input.txt", "r")
commands = [line.strip() for line in file]


def problem1():
    horizontal = 0
    deep = 0
    for command in commands:
        command = command.split()
        if command[0] == "forward":
            horizontal += int(command[1])
        elif command[0] == "down":
            deep += int(command[1])
        elif command[0] == "up":
            deep -= int(command[1])
    return horizontal * deep


def problem2():
    horizontal = 0
    deep = 0
    aim = 0
    for command in commands:
        command = command.split()
        if command[0] == "forward":
            horizontal += int(command[1])
            deep += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
    return horizontal * deep


print("Output of the first part: ", problem1())
print("Output of the second part: ", problem2())
