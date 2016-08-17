#Gives perimeter and area for vonkoche snowflake at "n" stage

user_input = int(raw_input("Stage num : "))
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
