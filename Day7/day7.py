import statistics
import math

crabs = open('input.txt').read()
crabs = [int(number) for number in crabs.split(',')]
median = int(statistics.median(crabs))
mean = round(statistics.mean(crabs)) - 1


def sum_of_next_numbers(x):
    sumn = 0
    for i in range(x + 1):
        sumn += i
    return sumn


fuel = 0
for crab in crabs:
    fuel += abs(crab - median)

print("Output of the first part: ", fuel)

fuel = 0
for crab in crabs:
    fuel += sum_of_next_numbers(abs(crab - mean))

print("Output of the second part: ", fuel)
