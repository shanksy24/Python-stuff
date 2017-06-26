#Prime Number Generator
import math
cap = raw_input("Input maximum number to be checked : ")
cap = int(cap)
subcap = 0

prime_list = [2,3,5]

print "Primes : "
for n in range(7,cap):
	subcap = int(math.sqrt(n))
	check = False

	for x in prime_list:
		if n%x == 0:
			check = True

	if check == False:
		prime_list =+ n
