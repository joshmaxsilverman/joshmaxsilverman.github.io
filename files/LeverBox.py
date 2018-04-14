State_Probs = {(9,1,1,1,1,1,1,1,1,1) : 1}

def Modified_State(State,Indexes):
	
	New_State_List = list(State)
	for i in Indexes:
		New_State_List[i] = 1
	New_State = tuple(New_State_List)
	return New_State

def Best_Case_Prob_For(State,Sum):
		
	Best_Case_Prob = 0

	if Sum < 10 and State[Sum] == 0:
		P = Prob_For_State(Modified_State(State,(Sum,)))
		if P > Best_Case_Prob:
			Best_Case_Prob = P

	for i in range(1, min(9,Sum)):
		j = Sum - i
		if j > 9 or i == j:
			continue
		try:
			if State[i] == 0 and State[j] == 0:
				P = Prob_For_State(Modified_State(State,(i,j)))
				if P > Best_Case_Prob:
					Best_Case_Prob = P
		except:
			print i,j,Sum,State
	for i in range(1, min(7,Sum)):
		for j in range(1, min(7,Sum)):
			k = Sum - i - j
			if k < 1 or k > 9 or i == j or j == k or i ==k:
				continue
			if State[i] == 0 and State[j] == 0 and State[k] == 0:
				P = Prob_For_State(Modified_State(State,(i,j,k)))
				if P > Best_Case_Prob:
					Best_Case_Prob = P
	return Best_Case_Prob


def Prob_For_State(State):
	global State_Probs 

	if State in State_Probs:
		return State_Probs[State]

	# Throw one die
	P1 = 0
	for i in range(1,7):
		P1 += 1.0/6 * Best_Case_Prob_For(State,i)

	# Throw two dice
	P2 = 0
	for i in range(1,7):
		for j in range(1,7):
			P2 += 1.0/36 * Best_Case_Prob_For(State,i+j)
	P = max(P1,P2)
	State_Probs[State] = P
	return P

print "P(000000000) =", Prob_For_State((9,0,0,0,0,0,0,0,0,0))
