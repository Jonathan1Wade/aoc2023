digit_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def translate(line):
    for num, name in enumerate(digit_names):
        line = line.replace(name, f"{name} {num} {name}")
    return line

with open('Day1/input.txt', 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        digits = [char for char in translate(line) if char.isnumeric()]
        if digits:
            total += int(digits[0]+digits[-1])
        
    print(total)
        

