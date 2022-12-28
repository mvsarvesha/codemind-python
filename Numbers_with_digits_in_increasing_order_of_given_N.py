# Python3 program to print all n-digit numbers
# whose digits are strictly increasing
# from left to right

# Function to print all n-digit numbers
# whose digits are strictly increasing
# from left to right.
# out --> Stores current output
#		 number as string
# start --> Current starting digit
#		 to be considered
def findStrictlyIncreasingNum(start, out, n):
	
	# If number becomes N-digit, print
	if (n == 0):
		print(out, end = " ")
		return

	# start from (prev digit + 1) till 9
	for i in range(start, 10):
		
		# append current digit to number
		str1 = out + str(i)

		# recurse for next digit
		findStrictlyIncreasingNum(i + 1,
							str1, n - 1)

# Driver code
n = int(input())
if n==1 :
    findStrictlyIncreasingNum(0, "", n)
else:
    findStrictlyIncreasingNum(1, "", n)

