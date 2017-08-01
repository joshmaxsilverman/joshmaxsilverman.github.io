# For fivethirtyeight.com Riddler. Search for longest path in divisor graph.
# This produces a path of length 75 in under 15 seconds when run with pypy.

N = 100
print "N:",N

# High primes and their multiples waste precious small connecting numbers.
dontUse = [37,74,41,82,43,86,47,94,53,59,61,67,71,73,79,83,89,97]

connected = [[]]
for i in range(N):
	connected.append([])
for m in range(1,N+1):
	# Prioritize larger neighbors
	for n in range(N,0,-1):
		if ((not m == n) and (m%n == 0 or n%m == 0) and not n in dontUse):
			connected[m].append(n)

def explore(path):
	global longestLength, longestPath, connected

	isExtendable = 0
	n = path[-1]
	# Prioritize numbers with few neighbors among the remaining numbers
	options = list(connected[n])
	options.sort(key=lambda x: len(set(connected[x])-set(path)))
	for m in options:
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

# Starting with 92 works best (trial and error).
explore([92])
