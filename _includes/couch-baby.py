from random import randint 

reps = 10000000
accum = 0
position = 0
for rep in range(reps):
	r = randint(1,4)
	if r == 1:
		position += 1
	elif r in [2,3]:
		position -= 1
	if position < 0:
		position = 0
	if position == 0:
		accum += 1

print(accum/reps)
