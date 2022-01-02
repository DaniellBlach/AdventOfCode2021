template, *pairs = open('input.txt').read().split('\n')
pairs = [pair.split('\n') for pair in pairs]


def sortByIndex(e):
    return e[2]


for i in range(10):
    results = []
    for pair in pairs:
        left, right = pair[0].split(' -> ')
        for k in range(len(template) - 1):
            if template[k] == left[0] and template[k + 1] == left[1]:
                results.append([left, right, k])
    results.sort(key=sortByIndex)

    for j, results in enumerate(results):
        index = results[2] + 1 + j
        template = template[:index] + results[1] + template[index:]
    print( len(template))

all_freq = {}

for i in template:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(max(all_freq.values()) - min(all_freq.values()))
