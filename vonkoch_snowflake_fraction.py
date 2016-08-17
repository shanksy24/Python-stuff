#Gives perimeter and area for vonkoche snowflake at "n" stage

user_input = int(raw_input("Stage num : "))
area_tally = [1,1]
area_total = [1,1]

if user_input == 0:
	print "Perimeter : 3 units"
	print "Area      : 1 unit squared"
	exit()

area_tally[0] *= 3 
area_tally[1] *= 9
print area_tally
print area_total

for n in range(1, user_input):
	area_tally[0] *= 4
	area_total[0] += area_tally[0]
	area_tally[1] *= 9
	area_total[1] += area_tally[1]
	print area_total

print "Area      : " + str(area_total[0]) + "/" + str(area_total[1]) + " units squared"

perimeter = 3 * (float(float(4)/float(3))**user_input)

print "Perimeter : " + str(perimeter) + " units"
