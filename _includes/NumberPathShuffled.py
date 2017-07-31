from random import shuffle
N = 100
shufflePeriod = 20000000
print(N)

connected = [[]]
for i in range(N):
	connected.append([])
for m in range(1,N+1):
	# for n in range(1,N+1):
	for n in range(N,0,-1):
		if ((not m == n) and (m%n == 0 or n%m == 0)):
			connected[m].append(n)

def explore(path):
	global longestLength, longestPath, connected, shuffleCounter, shufflePeriod

	shuffleCounter += 1
	if shuffleCounter == shufflePeriod:
		shuffleCounter = 0
		for L in connected:
			shuffle(L)
		print "Shuffled. Still",longestLength,longestPath

	isExtendable = 0
	n = path[-1]
	# shuffledconnected = list(connected[n])
	# shuffle(shuffledconnected)
	for m in connected[n]:
	#for m in shuffledconnected:
		if not m in path:
			isExtendable = 1
			newPath = list(path)
			newPath.append(m)
			explore(newPath)
	if not isExtendable:
		if len(path) > longestLength:
			longestLength = len(path)
			longestPath = path
			print longestLength,longestPath

longestPath = []
longestLength = 0

#for n in range(1,N+1):
#	print(n)
#	explore([n])

shuffleCounter = 0
explore([81])

print("Longest path length is",longestLength)
print(longestPath)
