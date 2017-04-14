from random import randint,uniform

reps = 10000000
accum = 0

Vacancies = [0,1,2,3,4,5,6,7,8]
Expiration = [reps]*9

for rep in range(reps):
	# rep is the number of 2-year periods that have passed.

	# Figure the average number of vacancies since
	# the last election, including new vacancies.
	AvgVacancies = len(Vacancies)
	NewExpiration = [reps]*9
	for i in range(9):
		if Expiration[i] <= rep:
			# Seat i has been vacated since last election
			if President == Senate:
				# Seat was filled as needed until expiring after 
				# this election, so it's now occupied
				NewExp = Expiration[i]
				while NewExp <= rep:
					NewExp += uniform(0,20)
				NewExpiration[i] = NewExp
			else:
				# Seat has been unfilled for (rep - Expiration[i]) reps
				AvgVacancies += (rep - Expiration[i])
				Vacancies.append(i)
		else:
			# Seat occupied
			NewExpiration[i] = Expiration[i]
	Expiration = NewExpiration
	accum += AvgVacancies

	# Hold elections
	Senate = randint(0,1)
	if rep/2 == int(rep/2):
		President = randint(0,1)

	# Fill empty seats
	if President == Senate:
		for i in Vacancies:
			Expiration[i] = rep + uniform(0,20)
		Vacancies = []

print(accum/reps)
