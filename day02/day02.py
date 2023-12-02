import math
import re

with open("input", "r") as f:
    file_input = f.read().splitlines()

max_cubes = {"red": 12, "green": 13, "blue": 14}
p1_sum = p2_sum = 0

for l in file_input:
    min_cubes = dict()
    for count, color in re.findall(r"(\d+) (\w+)", l):
        count = int(count)
        if count > min_cubes.get(color, 0): min_cubes[color] = count
    p2_sum += math.prod(min_cubes.values())
    if all(i <= max_cubes[color] for color, i in min_cubes.items()):
        p1_sum += int(re.search(r"(\d+):", l).group(1)) 

print("Part 1:", p1_sum)
print("Part 2:", p2_sum)

