DeckSize = 100
TotalDeals = 10

# Probability of winning if, not having held yet, we get card C with D 
# cards remaining to be dealt and H the highest card so far dealt 
#(including C): P[(C,D,H)]
P_Win = {}

# The true/false value of whether it's best to hold rather than discard
# in that situation: Hold[(C,D,H)]
Hold = {}

def GetP_Win(Card,StillToBeDealt,HighestSoFar):
	global P_Win,Hold,DeckSize,TotalDeals

	if (Card,StillToBeDealt,HighestSoFar) in P_Win:
		# already figured this one
		return P_Win[(Card,StillToBeDealt,HighestSoFar)]

	HaveBeenDealt = TotalDeals - StillToBeDealt
	# Assume we'll discard; change later if holding is better:
	Hold[(Card,StillToBeDealt,HighestSoFar)] = 0

	if StillToBeDealt == 0:
		# Card is the final card.
		if Card == HighestSoFar:
			P_Win[(Card,StillToBeDealt,HighestSoFar)] = 1
			return 1
		else:
			P_Win[(Card,StillToBeDealt,HighestSoFar)] = 0
			return 0

	RemainingSubHighest = max(HighestSoFar-(HaveBeenDealt-1),0)
	Remaining = DeckSize-HaveBeenDealt

	# Calculate probability of victory if we discard.
	# Probability is the average of probabilities in the next deal
	P_Discard = (1/Remaining) * (\
		RemainingSubHighest*GetP_Win(0,StillToBeDealt-1,HighestSoFar) + \
		sum([GetP_Win(C,StillToBeDealt-1,C) for C in range(HighestSoFar+1,DeckSize)]) \
		)
	# Calculate probability of victory if we hold.
	P_Hold = 1
	for i in range(StillToBeDealt):
		P_Hold *= (RemainingSubHighest-i)/(Remaining-i)
	if not Card == HighestSoFar or P_Discard > P_Hold:
		P_Win[(Card,StillToBeDealt,HighestSoFar)] = P_Discard
	else:
		P_Win[(Card,StillToBeDealt,HighestSoFar)] = P_Hold
		Hold[(Card,StillToBeDealt,HighestSoFar)] = 1
	return P_Win[(Card,StillToBeDealt,HighestSoFar)]

# Main Program

accum_prob = 0

for Card in range(DeckSize):
	accum_prob += GetP_Win(Card,TotalDeals-1,Card)

print("Overall probability of victory:",accum_prob/DeckSize)
print("Thresholds (card dealt : threshold to hold):")
for i in range(1,TotalDeals):
	for c in range(DeckSize):
		if Hold[(c,i,c)] == 1:
			# Remember that our cards start at 0
			print(i,":",c+1)
			break


