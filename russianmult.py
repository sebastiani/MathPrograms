#Python 2.7
#Composer: Sebastiani Aguirre
#russianmult.py
import sys


def mults(A,B):
	if A == 0:
		return 0
	else:

		if A%2 != 0:
			return B+mults(A/2, B*2)
		else:
			return mults(A/2, B*2)

try:
	A, B =  sys.argv[1].split(',')
	A =  int(A)
	B =  int(B)
	print mults(A,B)

except:
	print "Usage: python russianmult.py A,B"
