import re
import math

with open("input", "r") as f:
    schematic = f.read().splitlines()

def adj(y, x, bound_y, bound_x0, bound_x1):
    return x >= bound_x0-1 and x < bound_x1+1 and y >= bound_y-1 and y <= bound_y+1

symbols = []
numbers = []
for y, line in enumerate(schematic):
    symbols.extend((match.group(), (y, match.start())) for match in re.finditer(r"[^\d.]", line))
    numbers.extend((int(match.group()), (y, *match.span())) for match in re.finditer(r"\d+", line))

part_nums = [n for n in numbers if any(adj(*s_pos, *n[1]) for _, s_pos in symbols)]

p2_sum = 0
for _, star_pos in filter(lambda x: x[0] == "*", symbols):
    adj_nums = [i for i, bounds in part_nums if adj(*star_pos, *bounds)]
    if len(adj_nums) == 2: p2_sum += math.prod(adj_nums)

print("Part 1:", sum(i for i,_ in part_nums))
print("Part 2:", p2_sum)

