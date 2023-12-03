#PROMPT 
#Every line of a calibration document called Day1/input.txt is a line of text; 
#each line contains a value that is needed to be recovered. 
#On each line the value can be found by combining the first digit and the last digit (in that order)
#to form a two-digit number. If there is only one digit in the line of text e.g. 3fgr then the answer for that line is 33. 
#The script needs to calucate the sum of all the calibration values


# Read the input file
with open("Day1/input.txt", "r") as file:
    lines = file.readlines()

# Initialize the sum of calibration values
calibration_sum = 0

# Iterate over each line in the input file
for line in lines:
    # Remove any whitespace characters from the line
    line = line.strip()
    
    # Find the first and last digits in the line
    first_digit = None
    last_digit = None
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    
    # Combine the first and last digits to form a two-digit number
    if first_digit is not None and last_digit is not None:
        calibration_value = int(first_digit + last_digit)
    elif first_digit is not None:
        calibration_value = int(first_digit + first_digit)
    else:
        calibration_value = 0
    
    # Add the calibration value to the sum
    calibration_sum += calibration_value

# Print the sum of calibration values
print(calibration_sum)