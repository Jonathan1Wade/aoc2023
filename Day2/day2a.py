with open('Day2/input.txt', 'r') as file:
    data = file.read().splitlines()

possible_games = []
for line in data:
    game, cubes = line.split(':')
    game = int(game.split()[1])
    cubes = cubes.split(';')
    possible = True
    for cube_set in cubes:
        cube_set = cube_set.split(',')
        for cube in cube_set:
            cube = cube.strip().split()
            color = cube[1]
            count = int(cube[0])
            if color == 'red' and count > 12:
                possible = False
            elif color == 'green' and count > 13:
                possible = False
            elif color == 'blue' and count > 14:
                possible = False
    if possible:
        possible_games.append(game)

print(f"The possible games are: {possible_games}")
print(f"The sum of the IDs of the possible games is: {sum(possible_games)}")

# In this corrected version of the script, the color and count values for each cube are 
# correctly split and processed. You can try running this corrected script to see if it 
# solves the puzzle without errors. Let me know if you have any further issues or questions.