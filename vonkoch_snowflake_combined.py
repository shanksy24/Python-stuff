#Gives perimeter and area for vonkoche snowflake at "n" stage

user_input = int(raw_input("Stage num : "))

#fractional
area_tally = [1,1]
new_fractn = [9,9]
perimeter = [3,1]

if user_input == 0:
	print "Perimeter : 3 units"
	print "Area      : 1 unit squared"
	exit()

for n in range(1, user_input+1):
	if n == 1:
		area_tally = [4,3]
		
	else:
		area_tally[0] *= 9
		area_tally[1] *= 9
		area_tally[0] += (4**(n-1))

print "Area      : " + str(area_tally[0]) + "/" + str(area_tally[1]) + " units squared"

for n in range(user_input):
	perimeter[0] *= 4
	perimeter[1] *= 3

perimeter[0] /= 3
perimeter[1] /= 3


print "Perimeter : " + str(perimeter[0]) + "/" + str(perimeter[1]) + " units"

#decimal 
area_tally = 1

if user_input == 0:
	print "Perimeter : 3 units"
	print "Area      : 1 unit squared"
	exit()

for n in range(1, user_input+1):
	area_tally += (1/float(9**n)) * 3 * float(4**(int(n-1)))
  
print "Area      : " + str(area_tally) + " units squared"

perimeter = 3 * (float(float(4)/float(3))**user_input)

print "Perimeter : " + str(perimeter) + " units"
