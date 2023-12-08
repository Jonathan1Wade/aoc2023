# Thank you https://github.com/adriansliacky/adventofcode/blob/master/2023/05/main.py #


import re

# read the input file
with open('day5/input.txt', 'r') as f:
    lines = [line.split('\n') for line in f.read().split('\n\n')]

# function to create a map
def create_map(type_lines, prev_ranges):
    ranges = []
    for line in type_lines[1:]:
        to_dest_start, to_source_start, from_count = map(int, line.split())
        ranges.append([to_dest_start, to_source_start, from_count])
    broken_down_ranges = []
    for from_start, from_count in prev_ranges:
        while from_count > 0:
            have_range_match = False
            for to_dest_start, to_source_start, to_count in ranges:
                if to_source_start <= from_start < (to_source_start + to_count):
                    have_range_match = True
                    can_fit = to_count - (from_start - to_source_start)
                    if can_fit > from_count:
                        broken_down_ranges.append([to_dest_start + (from_start - to_source_start), from_count])
                        from_count = 0
                    else:
                        broken_down_ranges.append([to_dest_start + (from_start - to_source_start), can_fit])
                        from_count -= can_fit
                        from_start += can_fit
                    break
            if not have_range_match:
                broken_down_ranges.append([from_start, from_count])
                break
    return broken_down_ranges

# function to solve the puzzle
def solve(seeds_ranges):
    mp = create_map(lines[1], seeds_ranges)
    for i in range(2, len(lines)):
        mp = create_map(lines[i], mp)
    return min(mp, key=lambda x: x[0])[0]

# parse the seeds
SEEDS = list(map(int, re.findall(r'\d+', lines[0][0])))

# find the lowest location number
print(solve([[seed, 1] for seed in SEEDS]))