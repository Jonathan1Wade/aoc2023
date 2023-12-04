input_file = 'Day4/input.txt'
cards = open(input_file).read().split('\n')
total_points = 0


for card in cards:
    if card:
        card = card.split(':')[-1].strip()
        winning_numbers, my_numbers = card.split('|')
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))
        matches = [num for num in my_numbers if num in winning_numbers]
        points = 0
        for i in range(len(matches)):
            if i == 0:
                points += 1
            else:
                points *= 2
        total_points += points

print(f"The total number of points for the pile of scratchcards is: {total_points}")