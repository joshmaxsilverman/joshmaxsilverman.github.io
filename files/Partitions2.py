N = 14
P = 4
K = [0,0,0,0,0,0,0,0,0,0,0,1,2,3]
M = [0,0,0,0,0,0,0,0,0,0,0,1,2,3]

def GetNext(K,M):
	for i in range(N-1,0,-1):
		if K[i] < P-1 and K[i] <= M[i-1]:
			K[i] += 1
			M[i] = max(M[i],K[i])
			for j in range(i+1,N-(P-M[i])+1):
				K[j] = 0
				M[j] = M[i]
			for j in range(N-(P-M[i])+1,N):
				K[j] = M[j] = P-(N-j)
			return True
	return False

count = 1
while GetNext(K,M):
	count += 1
	pass
print count

