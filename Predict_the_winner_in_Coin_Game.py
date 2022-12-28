# Python implementation of the approach
# Function to print the winner of the game

def findWinner(M, N):
	if (M % 2 == 0 or N % 2 == 0):
		print("Player 1")
	else:
		print("Player 2")

# Driver code
M , N = input().split()
N = int(N)
M = int(M)
findWinner(M, N)
