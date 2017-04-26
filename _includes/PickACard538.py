from random import randint

num_reps = 1000000
accum = 0

Thresholds = [93,92,91,89,87,84,80,72,55,0]

for rep in range(num_reps):
	Deck = list(range(100)) # Cards from 0 to 99
	Hold = -1 # -1 is dummy value until we hold
	Highest = -1
	for deal in range(10):
		card = Deck.pop(randint(0,99-deal))
		if card > Highest:
			Highest = card
			# The thresholds are for cards numbered 1 to 100
			if Hold == -1 and card >= Thresholds[deal]-1:
			Hold = card
	if Hold == Highest:
		accum += 1

print(accum/num_reps)
