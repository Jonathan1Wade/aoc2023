import re

input_file = 'Day3/input.txt'
q = {3: open(input_file).read()}
num_coords = []
symbol_coords = []

for x, line in enumerate(q[3].split('\n')):
    nums = re.finditer(r'\d+', line)
    for n in nums:
        coords = []
        for i in range(len(n.group())):
            coords.append((x, n.start() + i))
        num_coords.append([n.group(), coords])
    symbols = re.finditer(r'[^.\d]', line)
    for s in symbols:
        symbol_coords.append([s.group(), (x, s.start())])

adj_nums = []
for n in num_coords:
    for c in n[1]:
        for s in symbol_coords:
            if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
                adj_nums.append(n) if n not in adj_nums else 0
                break

print(f"The sum of all of the part numbers in the engine schematic is: {sum([int(n[0]) for n in adj_nums])}")