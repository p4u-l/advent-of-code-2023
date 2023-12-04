import re, math, collections

with open("input", "r") as f:
    file_input = f.read().splitlines()

cards = [len(set(re.findall(r"\d+", l.split("|")[0].split(":")[1])) & set(re.findall(r"\d+", l.split("|")[1]))) for l in file_input]
print("Part 1:", sum(map(lambda x: math.floor(2**(x-1)), cards)))

to_process = collections.deque(range(len(cards)))
total = 0
while to_process:
    i = to_process.popleft()
    to_process.extend(range(i+1, i+cards[i]+1))
    total += 1
    
print("Part 2:", total)

