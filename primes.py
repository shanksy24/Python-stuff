# Calculates primes between two points
start_point = int(raw_input("Input starting number : "))
end_point = int(raw_input("Input end number : "))

list_of_nums = []
index = 1

for n in range(start_point, end_point):

	list_of_nums = []

	for counter in range(2, n):

		if n % counter == 0:
			list_of_nums.append(counter)
		elif n % counter != 0:
			pass

	if len(list_of_nums) > 0:
		pass
	else:
		print index, " : ", n
		index = index + 1

print "Success"
