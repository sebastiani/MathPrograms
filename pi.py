#Find nth digit of Pi
#Composer: Sebastiani Aguirre

#---------------------Notes------------------
#Chudnovsky-Ramanujan Equation(FFT)
#Must check how many integers can a python variable hold in order to keep a limit.


#---------------------------------------------
k1 = 545140134.0
k2 = 13591409.0
k3 = 820.2
k4 = 100100025.0
k5 = 327843840.0
k6 = 53360.0

def factorial(n):

	if n<1:
		return 1
	else:
		return n*factorial(n-1)

def power(n,pow):

	if pow <1:
		return 1
	else:
		return n*power(n,pow-1)

def pi(n):

	if n> 14:
		iterations =  n/14

	if n <=14:
		iterations = 1
	
	if n == 0:

		return (k6*k3)/(k2)

	else:
		if iterations%2 == 0:

			return (k6*k3)/(factorial(6*iterations)*(k2 + n*k1)/power(factorial(iterations),3)*factorial(3*iterations)*power(8*k4*k5, iterations))+ pi(iterations-1)
		else:
			return (-1)*(k6*k3)/(factorial(6*iterations)*(k2 + n*k1)/power(factorial(iterations),3)*factorial(3*iterations)*power(8*k4*k5, iterations))+ pi(iterations-1)

def outputPi(digits):

	return  str(pi(digits))[0:digits-1]

import sys

try: 
	print outputPi(int(sys.argv[1]))

except:
	print "Usage: python pi.py <Enter number of digits here>"
	sys.exit()
