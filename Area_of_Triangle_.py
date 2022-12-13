import math 
x,y,z = input().split()
s = (float(x)+float(y)+float(z))/2
area = math.sqrt(s* (s-float(x))*(s-float(y))*(s-float(z)))
print("{0:.2f}".format(area))