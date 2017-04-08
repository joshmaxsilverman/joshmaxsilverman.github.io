# fivethirtyeight.com Riddler https://fivethirtyeight.com/features/can-you-outsmart-our-elementary-school-math-problems/

# A situation is a tuple (A,B,C,D), representing AB*CD, where each element
# is a digit or -1 to represent an unfilled position.

# Strategy is a "dictionary" that contains optimal moves for pairs of
# a situation and a number (the number on the new card):
# E.g., Strategy[((A,B,C,D),N)] = 2 means that N should go in place of C.
Strategy = {}

# Expectation is a dictionary from situations to the expectation of them
# given optimal strategy.
Expectation = {}

def Process(situation):
	# Determine the optimal strategies for playing with this situation
	# and any next card, and generate the expectation of playing 
	# optimally starting from this situation.

	global Strategy, Expectation
	accum =  0
	num_newcards = 0
	for newcard in range(10):
		if newcard in situation:
			continue
		least_expected_product = [-1,10000]
		for i in range(4):
			if situation[i] == -1:
				sitlist = list(situation)
				sitlist[i] = newcard
				newsit = tuple(sitlist)
				if not -1 in newsit:
					Expectation[newsit] = \
						(10*newsit[0]+newsit[1])*(10*newsit[2]+newsit[3])
				elif not newsit in Expectation:
					Process(newsit)
				E = Expectation[newsit]
				if E < least_expected_product[1]:
					least_expected_product = [i,E]
		Strategy[(situation,newcard)] = least_expected_product[0]
		accum += least_expected_product[1]
		num_newcards += 1
	Expectation[situation] = accum/num_newcards

Process((-1,-1,-1,-1)) 

print("Optimal strategy expects",Expectation[(-1,-1,-1,-1)])
