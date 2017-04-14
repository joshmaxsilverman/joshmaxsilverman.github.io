from random import randint,uniform

num_reps = 10000000
accum = 0

# A running list of the vacant seats
Vacancies = [0,1,2,3,4,5,6,7,8]

# A list of the times justices in the 9 seats are due to retire
# or die yes I went there.
Expiration = [num_reps]*9

for rep in range(num_reps):
	# rep is the number of 2-year periods that have passed.

	# Figure the average number of vacancies since
	# the last election, including new vacancies.
	
	# If there were vacancies after the last election it's 
	# because there is not joint control, so those vacancies
	# remain. So the Average number of vacancies over this past
	# 2-year cycle is at least:
	AvgVacancies = len(Vacancies)

	# Create a new list for the expiration times seats will
	# have going into this election cycle.
	NewExpiration = [num_reps]*9
	for i in range(9):
		# Looping through the seats
		if rep-1 < Expiration[i] <= rep:
			# Seat i has been vacated since the last election
			if SameParty:
				# Seat was filled as needed until due to expire after 
				# this election, so it's been continuously occupied,
				# and adds nothing to average vacancies.
				NewExp = Expiration[i]
				while NewExp <= rep:
					# Seat went vacant again before now, so:
					NewExp += uniform(0,20)
				NewExpiration[i] = NewExp
			else:
				# Seat has been unfilled for (rep - Expiration[i]) reps,
				# adding that same amount to the average number of
				# vacancies since the last rep. Leaving its NewExpiration
				# value at num_reps is harmless.
				AvgVacancies += (rep - Expiration[i])
				# This is the only place we add to the list of vacancies.
				Vacancies.append(i)
		else:
			# Seat remains occupied or was already vacant as of the last 
			# election. In the former case, there's no effect on 
			# AvgVacancies, and it the latter we've already counted it.
			NewExpiration[i] = Expiration[i]
	Expiration = NewExpiration
	# We add up the average numbers of vacancies between reps, and will 
	# divide by num_reps to give the overall average.
	accum += AvgVacancies

	# Hold elections
	SameParty = randint(0,1)

	# Fill empty seats
	if SameParty:
		for i in Vacancies:
			Expiration[i] = rep + uniform(0,20)
		# This is the only place seats are removed from the vacancies list.
		Vacancies = []

print(accum/num_reps)
