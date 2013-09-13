#Prime factorization
#Composer: Sebastiani Aguirre

import sys

try:

	prime= []
	for i in range(2,int(sys.argv[1]):

		for j in range(2,i):

			if i%j == 0:
				continue
			else:
				prime.append(i)


	for k in range(prime.__len__()):

		for l in range(k, prime.__len__()):
			if prime[k]*prime[l] == sys.argv[1]:
				print prime[k], prime[l]

except:
	print "Usage: python primefact.py <number here>"
