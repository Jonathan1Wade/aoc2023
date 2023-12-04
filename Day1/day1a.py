#PROMPT 
#Every line of a calibration document called Day1/input.txt is a line of text; 
#each line contains a value that is needed to be recovered. 
#On each line the value can be found by combining the first digit and the last digit (in that order)
#to form a two-digit number. If there is only one digit in the line of text e.g. 3fgr then the answer for that line is 33. 
#The script needs to calucate the sum of all the calibration values


with open('Day1/input.txt', 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if len(digits) == 0:
            continue
        elif len(digits) == 1:
            total += int(digits[0] * 2)
        else:
            total += int(digits[0] + digits[-1])
    print(f"The sum of all the calibration values is: {total}")