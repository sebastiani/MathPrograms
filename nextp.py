#Next prime number
#Composer: Sebastiani Aguirre



def prime_finder(p):

	for n in range(2, p):
		if p%n == 0:
			p = "no prime"
			break
	return p

ans='y'


print 2
p =  prime_finder(3)
while ans[0].lower() == 'y':
	
	if p == "no prime":
		while p == 'no prime':
			state +=1
			p = prime_finder(state)
	print p
	state = p+1
	p = prime_finder(p+1)

	
	ans= raw_input("Next prime?[y/n]: ")