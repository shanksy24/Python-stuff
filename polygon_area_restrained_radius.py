from math import sin, pi , radians

n = raw_input("Amount of sides on polygon : ")

print float(n)

area = (float(n)/2.0) * (sin(radians(360.0/float(n))))

print "Area = ", area, "units squared"

pi_string = str(pi)
area_list = []
counter = 0

if area >= 3.1:
	for c in str(area):
		area_list.append(c)
	
	for index, c in enumerate(pi_string):
		if c == area_list[index]:
			counter += 1
		else:
			break
	
	print "Equal to pi, accurate to", counter-2, "decimal places"
