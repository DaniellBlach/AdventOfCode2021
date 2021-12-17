import statistics

lines = open('input.txt').read().splitlines()
pairs = ["()", "[]", "<>", "{}"]


def find_bad_chunks(lines, pairs):
    badChunks = []
    incomplete = lines.copy()
    for line in lines:
        stack = []
        for el in line:
            good = False
            for pair in pairs:
                if el == pair[0]:
                    stack.append(el)
                    good = True
                elif el == pair[1]:
                    if stack[-1] == pair[0]:
                        stack.pop()
                        good = True
            if not good:
                incomplete.remove(line)
                badChunks.append(el)
                break
    return badChunks, incomplete


badChunks, incomplete = find_bad_chunks(lines, pairs)


def problem1(badChunks):
    suma = 0
    for el in badChunks:
        if el == ")":
            suma += 3
        elif el == "]":
            suma += 57
        elif el == "}":
            suma += 1197
        elif el == ">":
            suma += 25137
    return suma


def complete_chunks(incomplete):
    results = []
    for line in incomplete:
        stack = []
        for el in line:
            for pair in pairs:
                if el == pair[0]:
                    stack.append(el)
                elif el == pair[1]:
                    if stack[-1] == pair[0]:
                        stack.pop()
        result = []
        for el in stack[::-1]:
            for pair in pairs:
                if el == pair[0]:
                    stack.pop()
                    result.append(pair[1])
        results.append(result)
    return results


def problem2(results):
    score = []
    for result in results:
        suma = 0
        for el in result:
            suma *= 5
            if el == ")":
                suma += 1
            elif el == "]":
                suma += 2
            elif el == "}":
                suma += 3
            elif el == ">":
                suma += 4
        score.append(suma)
    return statistics.median(score)


print("Output of the first part: ", problem1(badChunks))
print("Output of the second part: ", problem2(complete_chunks(incomplete)))
