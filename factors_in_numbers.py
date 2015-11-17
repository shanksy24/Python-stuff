# Calculates primes between two points
start_point = int(raw_input("Input starting number : "))
end_point = int(raw_input("Input end number : "))

for n in range(start_point, end_point):
	print n, " : ",
	for counter in range(1, n):
		if n % counter == 0:
			print counter, ", ",
	print ""

print "Success"
