import re

with open("input", "r") as f:
    file_input = f.read().splitlines()

digit_strings = {s: str(i+1) for i, s in enumerate(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"))}

def first_last(l):
    return (l[0], l[-1])

def combine_digits(a, b):
    return int(a + b)

print("Part 1:", sum(combine_digits(*first_last(re.findall(r'\d', line))) for line in file_input))

p2_numbers = [re.findall("(?=(\d|" + "|".join(digit_strings.keys()) + "))", line) for line in file_input]
print("Part 2:", sum(combine_digits(*map(lambda x: digit_strings.get(x, x), first_last(nums))) for nums in p2_numbers))

