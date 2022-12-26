# Recursive function to return gcd of a and b
def gcd(a, b):

	# Everything divides 0
	if (a == 0):
		return b
	if (b == 0):
		return a

	# base case
	if (a == b):
		return a

	# a is greater
	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)

# Driver program to test above function
a,b = input().split()
a = int(a)
b = int(b)

print(gcd(a,b))