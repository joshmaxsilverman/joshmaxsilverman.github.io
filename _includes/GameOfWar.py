# Attempted solotion of Riddler at https://fivethirtyeight.com/features/riddler-nation-goes-to-war/

from random import shuffle

Reps = 1000000
Accum = 0
# How many cards go face-down in a tie-break?
CardsDown = 1

# Play the next cards and break any ties. Return True if
# there are more cards to play. Result is 1 if the aces
# player (me) wins the game.
def NextRound():
	global Me,You,Result,CardsDown
	Pot = []
	Done = False
	while not Done:
		MyCard = Me.pop()
		YourCard = You.pop()
		Pot.extend([MyCard,YourCard])
		shuffle(Pot)
		if MyCard < YourCard:
			# My card beats yours (lower number = higher card)
			# So I get the pot of played cards.
			Me = Pot + Me
			# No tie to be broken
			Done = True
			if len(You) == 0:
				# You lose
				Result = 1
			else:
				# You have more cards to play
				Result = 0
		elif YourCard < MyCard:
			You = Pot + You
			Done = True
			if len(Me) == 0:
				Result = 2
			else: 
				Result = 0
		else:
			# A tie.
			if len(Me) < 1 + CardsDown:
				# I don't have enough cards to play the tiebreak
				Done = True
				Result = 2
			elif len(You) < 1 + CardsDown:
				Done = True
				Result = 1
			else:
				# Play the tie-break, by first laying down the face-down
				# cards and then continuing the "while not Done" loop
				for i in range(CardsDown):
					Pot.extend([Me.pop(),You.pop()])
	return (Result == 0)

# You have four of every number from 1 to 12, while I have just four 0s
YourCards = []
for i in range(12):
	YourCards.extend([i+1]*4)

# Main loop
for Rep in range(Reps):
	Me = [0,0,0,0]
	You = list(YourCards)
	shuffle(You)
	while NextRound():
		continue
	if Result == 1:
		Accum += 1

print 1.0*Accum/Reps
