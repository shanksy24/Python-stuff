from math import tan, radians

n = raw_input("Amount of sides on end shape : ")
s = raw_input("Side Length : ")
h = raw_input("Height : ")

sa = 2.0*float(n)*((float(s)*((float(s)/2.0)/tan(radians(180.0/float(n)))))/2.0)+(float(s)*float(h)*float(n))

print "\nSurface Area = ", str(sa), "units squared"

print tan(radians(9))
