from random import shuffle

Reps = 1000000
Accum = 0
CardsDown = 1

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
			Me = Pot + Me
			Done = True
			if len(You) == 0:
				Result = 1
			else:
				Result = 0
		elif YourCard < MyCard:
			You = Pot + You
			Done = True
			if len(Me) == 0:
				Result = 2
			else: 
				Result = 0
		else:
			if len(Me) < 1 + CardsDown:
				Done = True
				Result = 2
			elif len(You) < 1 + CardsDown:
				Done = True
				Result = 1
			else:
				for i in range(CardsDown):
					Pot.extend([Me.pop(),You.pop()])
	return Result

YourCards = []
for i in range(12):
	YourCards.extend([i+1]*4)
for Rep in range(Reps):
	Me = [0,0,0,0]
	You = list(YourCards)
	shuffle(You)
	while NextRound() == 0:
		continue
	if Result == 1:
		Accum += 1

print 1.0*Accum/Reps
