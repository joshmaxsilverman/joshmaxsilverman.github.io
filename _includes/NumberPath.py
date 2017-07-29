N = 40

connected = [[]]
for i in range(N):
	connected.append([])
for m in range(1,N+1):
	for n in range(1,N+1):
		if ((not m == n) and (m%n == 0 or n%m == 0)):
			connected[m].append(n)

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

longestPath = []
longestLength = 0

for n in range(1,N+1):
	print(n)
	explore([n])

print("Longest path length is",longestLength)
print(longestPath)