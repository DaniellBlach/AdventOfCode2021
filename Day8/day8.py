lines = open('input.txt').read().splitlines()

sumdigit = 0
for line in lines:
    left, right = line.split(' | ')
    right = right.split(' ')
    for r in right:
        if len(r) == 2 or len(r) == 4 or len(r) == 3 or len(r) == 7:
            sumdigit += 1

print("Output of the first part: ", sumdigit)

####Part 2
"""""
#It just print a code
def print_code(list):
    print(" ", list[0], list[0], list[0])
    print(list[1], "     ", list[2])
    print(list[1], "     ", list[2])
    print(" ", list[3], list[3], list[3])
    print(list[4], "     ", list[5])
    print(list[4], "     ", list[5])
    print(" ", list[6], list[6], list[6])
"""""


def find_numers(list):
    zero = ''.join(sorted(list[0] + list[1] + list[2] + list[4] + list[5] + list[6]))
    one = ''.join(sorted(list[2] + list[5]))
    two = ''.join(sorted(list[0] + list[2] + list[3] + list[4] + list[6]))
    three = ''.join(sorted(list[0] + list[2] + list[3] + list[5] + list[6]))
    four = ''.join(sorted(list[1] + list[2] + list[3] + list[5]))
    five = ''.join(sorted(list[0] + list[1] + list[3] + list[5] + list[6]))
    six = ''.join(sorted(list[0] + list[1] + list[3] + list[4] + list[5] + list[6]))
    seven = ''.join(sorted(list[0] + list[2] + list[5]))
    eight = ''.join(sorted(list[0] + list[1] + list[2] + list[3] + list[4] + list[5] + list[6]))
    nine = ''.join(sorted(list[0] + list[1] + list[2] + list[3] + list[5] + list[6]))
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    return (numbers)


def create_list(left):
    ustr, alph = "", "abcdefg"
    list = [0] * 7
    for l in left:
        if len(l) == 2:
            ustr += l[0] + l[1]
            list[2] = l[0]
            list[5] = l[1]
        if len(l) == 3:
            for s in l:
                if s not in ustr:
                    list[0] = s
                    ustr += s
        if len(l) == 4:
            four = ""
            for s in l:
                if s not in ustr:
                    four += s
                    ustr += s
            list[3] = four[0]
            list[1] = four[1]
        if len(l) == 6 and list[0] in l and list[1] in l and list[2] in l and list[3] in l and list[5] in l:
            for s in l:
                if s not in ustr:
                    ustr += s
                    list[6] = s
    for a in alph:
        if a not in ustr:
            list[4] = a
    return list


def decode_value(output, right, numbers):
    for i, r in enumerate(right):
        for index, number in enumerate(numbers):
            if number == ''.join(sorted(r)):
                output[i] = index
    return output


def change_values_from_list(i, j, list):
    help = list[i]
    list[i] = list[j]
    list[j] = help
    return find_numers(list)


outputs = []
for line in lines:
    left, right = line.split(' | ')
    left = left.split(' ')
    right = right.split(' ')
    left = sorted(left, key=len)
    list = create_list(left)
    numbers = find_numers(list)
    output = [-1000] * 4
    output = decode_value(output, right, numbers)
    for so in output:
        if so == -1000:
            numbers = change_values_from_list(2, 5, list)
            break

    output = decode_value(output, right, numbers)
    for so in output:
        if so == -1000:
            numbers = change_values_from_list(1, 3, list)
            break

    output = decode_value(output, right, numbers)
    for so in output:
        if so == -1000:
            numbers = change_values_from_list(2, 5, list)
            break
    output = decode_value(output, right, numbers)
    outputs.append(output)

suma = 0
for output in outputs:
    val = int(''.join(map(str, output)))
    suma += val

print("Output of the second part: ", suma)
