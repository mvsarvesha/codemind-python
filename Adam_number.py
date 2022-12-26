# Python program to check Adam Number
# To reverse Digits of numbers
def reverseDigits(num) :
	rev = 0
	while (num > 0) :
		rev = rev * 10 + num % 10
		num //= 10
		
	return rev

# To square number
def square(num) :
	return (num * num)
	
# To check Adam Number
def checkAdamNumber(num) :
	
	# Square first number and square
	# reverse digits of second number
	a = square(num)
	b = square(reverseDigits(num))
		
	# If reverse of b equals a then given
	# number is Adam number
	if (a == reverseDigits(b)) :
		return True
	else :
		return False

# Driver program to test above functions
num = int(input())
if (checkAdamNumber(num)) :
	print ("True")
else :
	print ("False")



