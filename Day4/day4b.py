input_file = 'Day4/input.txt'
cards = open(input_file).read().split('\n')
total_cards = [1] * len(cards)
for i, card in enumerate(cards):
    if card:
        card = card.split(':')[-1].strip()
        winning_numbers, my_numbers = card.split('|')
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))
        matches = [num for num in my_numbers if num in winning_numbers]
        for j in range(i+1, min(i+1+len(matches), len(cards))):
            total_cards[j] += total_cards[i]
print(f"The total number of scratchcards is: {sum(total_cards)}")