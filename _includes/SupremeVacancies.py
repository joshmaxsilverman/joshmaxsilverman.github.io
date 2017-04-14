from random import randint,uniform

reps = 1000000
accum = 0

President = 0
Vacancies = 9
Expiration = [reps]*9

for rep in range(reps):
	# rep is the number of 2-year periods that have passed.

	# Figure the average number of vacancies since
	# the last election, including new vacancies.
	AvgVacancies = Vacancies
	NewExpiration = [reps]*9
	j = 0
	for i in range(9-Vacancies):
		if Expiration[i] < rep:
			if President == Senate:
				NewExpiration[j] = rep + uniform(0,20)
				j += 1
			else:
				AvgVacancies += rep - Expiration[i]
				Vacancies += 1
		else:
			NewExpiration[j] = Expiration[i]
			j += 1
	Expiration = NewExpiration

	accum += AvgVacancies

	# Hold elections
	Senate = randint(0,1)
	if rep/2 == int(rep/2):
		President = randint(0,1)

	# Fill empty seats
	if President == Senate:
		for i in range(9-Vacancies,9):
			Expiration[i] = rep + uniform(0,20)
			Vacancies -= 1

print(accum/reps)
