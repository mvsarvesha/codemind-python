# Python3 implementation of the above approach

# Function to find the
# number of digits in the integer
def digitsCount(n) :
	length = 0;
	while (n > 0) :
		length += 1
		n //= 10;
		
	return length


# Function to find the absolute difference
def absoluteFirstLast(n, x) :
	
	# Store the last x digits in last
	i = 0 
	mod = 1
	while (i < x) :
		mod *= 10
		i += 1;
	
	last = n % mod
	
	# Count the no. of digits in N
	length = digitsCount(n)
	
	# Remove the digits except the first x
	while (length != x) :
		n //= 10
		length -= 1
	
	# Store the first x digits in first
	first = n
	
	# Return the absolute difference between
	# the first and last
	return abs(first - last)

# Driver code
if __name__ == "__main__" :
	
	n, x =input().split()
	n = int(n)
	x = int(x)
	print(absoluteFirstLast(n, x))
	

