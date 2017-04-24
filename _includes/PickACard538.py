from random import randint,uniform

num_reps = 1000000

accum = 0

Thresholds = [93,93,92,90,88,86,82,74,55,0]

for rep in range(num_reps):
	Deck = list(range(100))
	Hold = 100
	Highest = 0
	for deal in range(10):
		card = Deck[randint(0,99-deal)]
		Deck.remove(card)
		if card > Highest:
			Highest = card
		if Hold == 100 and card >= Thresholds[deal]:
			Hold = card
	if Hold == Highest:
		accum += 1

print(accum/num_reps)



