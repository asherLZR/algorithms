import random

#numbers = [i for i in range(1, 10**8)]
n = 200000
n = 200000
with open('randomPowers.txt','w') as f:
	f.write(str(n)+'\n')
	f.write(' '.join([str(random.randint(100000,n)) for _ in range(n)]))
