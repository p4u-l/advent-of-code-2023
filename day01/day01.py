import re

with open("input", "r") as f:
    file_input = f.read().splitlines()

digit_strings = {s: str(i+1) for i, s in enumerate(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"))}

def first_last(l):
    return l[0], l[-1]

def combine_digits(a, b):
    return int(a + b)

p1_sum = sum(combine_digits(*first_last(re.findall(r'\d', l))) for l in file_input)
print("Part 1:", p1_sum)

p2_sum = 0

for l in file_input:
    nums = re.findall(rf"(?=(\d|{'|'.join(digit_strings.keys())}))", l)
    p2_sum += combine_digits(*map(lambda x: digit_strings.get(x, x), first_last(nums)))

print("Part 2:", p2_sum)

