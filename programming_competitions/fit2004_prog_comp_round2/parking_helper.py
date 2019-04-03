import random

#numbers = [i for i in range(1, 10**8)]
n = 100_000
t = 1_000_000_000
with open('c_parking.txt','w') as f:
	f.write(str(n)+'\n')
	f.write(' '.join([str(random.randint(1, t)) for _ in range(n)]))
