# For fivethirtyeight.com Riddler. Search for longest path in divisor graph.
# This produces a path of length 75 for N=100 and 551 for N=1000.

#N=100
N = 1000
print "N:",N

# High primes waste precious small connecting numbers.
#dontUse = {}
dontUse = [ 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
#dontUse = [ 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
#for n in dontUse:
#	i = 2
#	while i*n <= 1000:
#		dontUse.append(i*n)
#		i += 1
allUsable = list(set(range(1,N+1))-set(dontUse))

connected = [[]]
for i in range(N):
	connected.append([])
for m in allUsable:
	# Prioritize larger neighbors
	for n in list(reversed(allUsable)):
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
			print "Unused:", list(set(range(1,N+1)) - set(dontUse) - set(path))

longestPath = []
longestLength = 0

# 58, 62, and 92 yield paths of 75
#explore([92])
explore([964])
