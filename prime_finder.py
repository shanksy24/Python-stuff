#Prime Number Generator
import math
cap = raw_input("Input maximum number to be checked : ")
cap = int(cap)
subcap = 0

print "Primes : "
for n in range(2,cap):
	subcap = int(math.sqrt(n))
	check = False

	for x in range(2,n):
		if n%x == 0:
			check = True

	if check == False:
		print n 
