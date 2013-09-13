'''
Problem A. Store Credit
Input:
	The first line of input is the number of cases N
	--For each case--
	One line containing C, the amount of store credit
	One line containing the value I, the number of items
	One line containing space separated integers P, the price of an item
	Each test case will have exactly one solution
Output:
	One line containing Case #x followed by the indices of the items
'''
def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                            # Until all elements are partitioned...

        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.

            if bottom == top:                  # If we hit the top...
                done = 1                       # ... we are done.
                break

            if list[bottom] > pivot:           # Is the bottom out of place?
                list[top] = list[bottom]       # Then put it at the top...
                break                          # ... and start searching from the top.

        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.
            
            if top == bottom:                  # If we hit the bottom...
                done = 1                       # ... we are done.
                break

            if list[top] < pivot:              # Is the top out of place?
                list[bottom] = list[top]       # Then put it at the bottom...
                break                          # ...and start searching from the bottom.

    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point


def quicksort(list, start, end):
    if start < end:                            # If there are two or more elements...
        split = partition(list, start, end)    # ... partition the sublist...
        quicksort(list, start, split-1)        # ... and sort both halves.
        quicksort(list, split+1, end)
    else:
        return


import sys
f = open(sys.argv[1], 'r').readlines()

cases = range(1, int(f[0])+1)
credits = f[1::3]
items = f[2::3]
prices =f[3::3]
prices = [price.split() for price in prices] 

prices = [map(int,x) for x in prices]
[quicksort(prices[i],0, prices[i].__len__()-1) for i in range(3)]

for case in cases:
	credit = int(credits[case-1])
	print credit
	
	for price in prices[case-1]:
		if credit-price in prices[case-1]:
			print "Case#",+case,": ", prices[case-1].index(price)," ",prices[case-1].index(credit-price)
			break	
	
