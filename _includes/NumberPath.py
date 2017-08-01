# For fivethirtyeight.com Riddler. Search for longest path in divisor graph.
# This produces a path of length 74 in a few seconds when run with pypy.

N = 100
print "N:",N

connected = [[]]
for i in range(N):
	connected.append([])
for m in range(1,N+1):
	for n in range(N,0,-1):
		if ((not m == n) and (m%n == 0 or n%m == 0)):
			connected[m].append(n)

# Prioritize poorly-connected neighbors
for n in range(1,N+1):
	connected[n].sort(key=lambda x:len(connected[x]))

def explore(path):
	global longestLength, longestPath, connected

	isExtendable = 0
	n = path[-1]
	for m in connected[n]:
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

explore([92])
for n in range(100,1,-1):
	print n
	explore([n])
