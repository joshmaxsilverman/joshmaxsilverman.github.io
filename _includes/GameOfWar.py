from random import shuffle

Reps = 10000000
Accum = 0

def NextRound():
	global Me,You,Result
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
			if len(Me) < 2:
				Done = True
				Result = 2
			elif len(You) < 2:
				Done = True
				Result = 1
			else:
				Pot.extend([Me.pop(),You.pop()])

for Rep in range(Reps):
	Me = [0,0,0,0]
	You = []
	for i in range(12):
		You.extend([i+1]*4)
	shuffle(You)
	while True:
		NextRound()
		if Result == 0:
			continue
		elif Result == 1:
			Accum += 1
		break

print 1.0*Accum/Reps
