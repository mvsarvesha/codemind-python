# Python3 program to check a number
# is a Happy number or not

# Utility method to return
# sum of square of digit of n
def numSquareSum(n):
	squareSum = 0
	while(n):
		squareSum += (n % 10) * (n % 10)
		n = int(n / 10)
	return squareSum

# method return true if
# n is Happy number
def isHappynumber(n):

	# initialize slow
	# and fast by n
	slow = n
	fast = n
	while(True):
		
		# move slow number
		# by one iteration
		slow = numSquareSum(slow)

		# move fast number
		# by two iteration
		fast = numSquareSum(numSquareSum(fast))
		if(slow != fast):
			continue
		else:
			break

	# if both number meet at 1,
	# then return true
	return (slow == 1)

# Driver Code
n = int(input())
if (isHappynumber(n)):
	print("True");
else:
	print("False")

