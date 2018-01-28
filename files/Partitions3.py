from copy import deepcopy

N = 14

First = [0,0,0,0]
Lim = []
for _ in range(N):
	Lim.append(0)

def Explore(Current,Digit,First,Lim):
	for i in range(0,Lim[Digit]+1):
		L = Current
		L[Digit] = i
		if Digit == LastFree:
			Partitions.append(L)
		else:
			NewDigit = Digit + 1
			Done = False
			while NewDigit in First:
				if NewDigit >= N-1:
					Done = True
					break
				NewDigit += 1
			if not Done:
				Explore(L,NewDigit,First,Lim)

Partitions = []
for First[1] in range(1,N-2):
	for i in range(1,First[1]):
		Lim[i] = 0
	for First[2] in range(First[1]+1,N-1):
		for i in range(First[1]+1,First[2]):
			Lim[i] = 1
		for First[3] in range(First[2]+1,N):
			for i in range(First[2]+1,First[3]):
				Lim[i] = 2
			for i in range(First[3]+1,N):
				Lim[i] = 3
			Current = [0]*N
			for j in range(4):
				Current[First[j]] = j
			LastFree = N-1
			while LastFree in First:
				LastFree -= 1
			for j in range(1,N):
				if Current[j] == 0:					
					Explore(Current,j,First,Lim)
					break

print len(Partitions),"partitions"
#print Partitions



