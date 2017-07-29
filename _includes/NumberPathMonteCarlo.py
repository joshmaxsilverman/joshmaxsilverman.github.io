from random import randint

N = 100
reps = 1000000

connected = [[]]
for i in range(N):
	connected.append([])
for m in range(1,N+1):
	for n in range(1,N+1):
		if ((not m == n) and (m%n == 0 or n%m == 0)):
			connected[m].append(n)

def explore(path):
	global longestLength, longestPath, connected
	n = path[-1]
	neighbors = [x for x in connected[n] if not x in path]
	if neighbors == []:
		if len(path) > longestLength:
			longestLength = len(path)
			longestPath = path
			print(longestLength)
	else:
		newPath = list(path)
		newPath.append(neighbors[randint(0,len(neighbors)-1)])
		explore(newPath)

longestPath = []
longestLength = 0

for rep in range(reps):
	explore([randint(1,N)])

print("Longest path length is",longestLength)
print(longestPath)