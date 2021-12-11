from collections import Counter


class lanternfish:
    def __init__(self, daysUntilNewFish):
        self.daysUntilNewFish = daysUntilNewFish

    def reproduce(self):
        if self.daysUntilNewFish == 0:
            self.daysUntilNewFish = 6
            return True
        else:
            self.daysUntilNewFish -= 1
            return False


class shoal:
    def __init__(self, howManyFishes):
        self.howManyFishes = howManyFishes


numbers = open('input.txt').read()
lanternfishes = [lanternfish(int(number)) for number in numbers.split(',')]

for i in range(1, 81):
    for fish in lanternfishes:
        if fish.reproduce():
            lf = lanternfish(9)
            lanternfishes.append(lf)

print("Output of the first part: ", len(lanternfishes))

numbers = [int(number) for number in numbers.split(',')]
counter = Counter(numbers)

shoals = []
for i in range(9):
    shoals.append(shoal(counter[i]))

for j in range(1, 257):
    tempList = [0] * 9
    for i, sh in enumerate(shoals):
        if i == 0:
            tempList[6] = shoal(sh.howManyFishes + shoals[7].howManyFishes)
            tempList[8] = shoal(sh.howManyFishes)
        elif i != 7 and i != 9:
            tempList[i - 1] = shoal(sh.howManyFishes)
    shoals = tempList

print("Output of the second part: ", sum([shoal.howManyFishes for shoal in shoals]))
