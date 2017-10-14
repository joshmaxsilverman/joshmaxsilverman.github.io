N = 100
for Strategy in ("always rush","always pass","optimal"):
	E = {}
	for m in range(2*N+1):
		for y in range(max(0,N-m),2*N-m+1):
			if m>y:
				E[(N,m,y)] = 1
			elif y>m:
				E[(N,m,y)] = 0
			else:
				E[(N,m,y)] = .5
	E_Naive = dict(E)
	for t in range(N-1,-1,-1):
		if t%2 and not Strategy == "optimal":
			continue
		for m in range(2*t+1):
			for y in range(max(0,t-m),2*t-m+1):
				if Strategy == "always rush":
					E_rush = .25*E[(t+2,m+1,y+1)]+.25*E[(t+2,m+2,y)] + .25*E[(t+2,m,y+2)]+.25*E[(t+2,m+1,y+1)]
					E_pass = .25*E[(t+2,m+2,y+1)]+.25*E[(t+2,m+3,y)] + .25*E[(t+2,m,y+3)]+.25*E[(t+2,m+1,y+2)]
					E_Naive_rush = .25*E_Naive[(t+2,m+1,y+1)]+.25*E_Naive[(t+2,m+2,y)] + .25*E_Naive[(t+2,m,y+2)]+.25*E_Naive[(t+2,m+1,y+1)]
					E_Naive_pass = .25*E_Naive[(t+2,m+2,y+1)]+.25*E_Naive[(t+2,m+3,y)] + .25*E_Naive[(t+2,m,y+3)]+.25*E_Naive[(t+2,m+1,y+2)]
				elif Strategy == "always pass":					
					E_rush = .25*E[(t+2,m+1,y+2)]+.25*E[(t+2,m+3,y)] + .25*E[(t+2,m,y+3)]+.25*E[(t+2,m+2,y+1)]
					E_pass = .25*E[(t+2,m+2,y+2)]+.25*E[(t+2,m+4,y)] + .25*E[(t+2,m,y+4)]+.25*E[(t+2,m+2,y+2)]				
					E_Naive_rush = .25*E_Naive[(t+2,m+1,y+2)]+.25*E_Naive[(t+2,m+3,y)] + .25*E_Naive[(t+2,m,y+3)]+.25*E_Naive[(t+2,m+2,y+1)]
					E_Naive_pass = .25*E_Naive[(t+2,m+2,y+2)]+.25*E_Naive[(t+2,m+4,y)] + .25*E_Naive[(t+2,m,y+4)]+.25*E_Naive[(t+2,m+2,y+2)]
				elif Strategy == "optimal":
					E_rush = 1 - .5*E[(t+1,y,m+1)] - .5*E[(t+1,y+1,m)]
					E_pass = 1 - .5*E[(t+1,y,m+2)] - .5*E[(t+1,y+2,m)]
					E_Naive_rush = 1 - .5*E_Naive[(t+1,y,m+1)] - .5*E_Naive[(t+1,y+1,m)]
					E_Naive_pass = 1 - .5*E_Naive[(t+1,y,m+2)] - .5*E_Naive[(t+1,y+2,m)]
				E[(t,m,y)] = max(E_rush,E_pass)
				if t%2:
					E_Naive[(t,m,y)] = max(E_Naive_rush,E_Naive_pass)
				else:
					if m > y:
						E_Naive[(t,m,y)] = E_Naive_rush
					else:
						E_Naive[(t,m,y)] = E_Naive_pass
	print "If opponent's strategy is",Strategy,"first player's expectation is", E[(0,0,0)]
	print "    and first player playing naive strategy expects",E_Naive[(0,0,0)]
