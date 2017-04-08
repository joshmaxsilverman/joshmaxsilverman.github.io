from random import randint

def RemainingAverage2(A,B):
	# The average of the remaining numbers now that A, B, and C are gone
	return (45 - A - B)/8

def RemainingAverage3(A,B,C):
	# The average of the remaining numbers now that A, B, and C are gone
	return (45 - A - B - C)/7

HighHigh = [10,9]
MidHigh = [7]
LowHigh = [5,6]
HighLow = [3,4]
MidLow = [2]
LowLow = [0,1]

reps = 1000000
accum = 0
for rep in range(reps):
	# Generate four random integers between 0 and 9
	A = randint(0,9)
	B = A
	while B == A:
		B = randint(0,9)
	C = A
	while C == A or C == B:
		C = randint(0,9)
	D = A
	while D == A or D == B or D == C:
		D = randint(0,9)

	if A < 5:
		UpLeft = A
		if B < RemainingAverage2(A,B):
			# A and B both Low numbers
			DownLeft = B
			if C < RemainingAverage3(A,B,C):
				# Couple C with the lower of A and B
				if A < B:
					UpRight = C
					DownRight = D
				else:
					UpRight = D
					DownRight = C
			else:
				if A > B:
					UpRight = C
					DownRight = D
				else:
					UpRight = D
					DownRight = C
		elif (A in HighLow and B in HighHigh) \
			or (A in LowLow and B in LowHigh) \
			or (A in MidLow or B in MidHigh):
			# A and B "match" in being high or low in their range, or one is middling
			UpRight = B
			if C < RemainingAverage3(A,B,C):
				DownLeft = C
				DownRight = D
			else:
				DownLeft = D
				DownRight = C
		else:
			# A in HighLow and B in LowHigh or A in LowLow and B in HighHigh
			DownRight = B
			if C < RemainingAverage3(A,B,C):
				DownLeft = C
				UpRight = D
			else:
				DownLeft = D
				UpRight = C
	else:
		# A is a High number
		UpRight = A
		if B >= RemainingAverage2(A,B):
			DownRight = B
			if A > B:
				if C > RemainingAverage3(A,B,C):
					UpLeft = C
					DownLeft = D
				else:
					DownLeft = C
					UpLeft = D
			else:
				if C < D: 
					UpLeft = C
					DownLeft = D
				else:
					DownLeft = C
					UpLeft = D
		elif (A in HighHigh and B in HighLow) \
			or (A in LowHigh and B in LowLow) \
			or (A in MidHigh or B in MidLow):
			UpLeft = B
			if C < RemainingAverage3(A,B,C):
				DownLeft = C
				DownRight = D
			else:
				DownLeft = D
				DownRight = C
		else:
			# A in HighHigh and B in LowLow or A in LowHigh and B in HighLow
			DownLeft = B
			if C < RemainingAverage3(A,B,C):
				UpLeft = C
				DownRight = D
			else:
				DownRight = C
				UpLeft = D
	accum += (10*UpLeft + UpRight)*(10*DownLeft + DownRight)

print(accum/reps)
 
