import random

def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)

def mod_exp(x, y, N): 
	if y == 0:
		return 1
	z = mod_exp(x,y//2,N)
	if y % 2 != 0:
		return (x*z**2) % N
	else:
		return (z**2) % N
	 
def fprobability(k):
    return 1 - .5**k

def mprobability(k):
    return 1 - .25**k

def fermat(N,k):
	a = random.randint(2,N-1)
	for i in range(k):
		if mod_exp(a, N-1, N) == 1:
			continue
		else:
			return 'composite'
	return 'prime'

def miller_rabin(N,k):
	for i in range(k):
		p = (N-1)*2
		a = random.randint(2,N-1)
		while p > 1 and p % 2 == 0:
			p = p / 2
			m = mod_exp(a,p,N)
			if m != 1:
				if m == N-1:
					break
				else:
					return 'composite'

	return 'prime'
