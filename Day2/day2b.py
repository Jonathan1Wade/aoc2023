with open('Day2/input.txt', 'r') as file:
    data = file.read().splitlines()

min_cubes = []
for line in data:
    game, cubes = line.split(':')
    game = int(game.split()[1])
    cubes = cubes.split(';')
    min_red = 0
    min_green = 0
    min_blue = 0
    for cube_set in cubes:
        cube_set = cube_set.split(',')
        red = 0
        green = 0
        blue = 0
        for cube in cube_set:
            cube = cube.strip().split()
            color = cube[1]
            count = int(cube[0])
            if color == 'red':
                red = count
            elif color == 'green':
                green = count
            elif color == 'blue':
                blue = count
        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)
    min_cubes.append((min_red, min_green, min_blue))

powers = [red * green * blue for red, green, blue in min_cubes]
print(f"The minimum set of cubes for each game is: {min_cubes}")
print(f"The power of each set of cubes is: {powers}")
print(f"The sum of the power of the sets of cubes is: {sum(powers)}")

# This updated script calculates the minimum number of cubes of each color that must have been 
# present in the bag for each game to be possible. The power of each set of cubes is calculated 
# as the product of the number of red, green, and blue cubes. The final result is the sum of the 
# power of all the sets of cubes. You can run this updated script to solve the new challenge. 
# Let me know if you have any further questions or issues.