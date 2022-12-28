def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a
 
# Function to check if a number
# is ugly or not
def isUgly(no):
    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)
    return 1 if no == 1 else 0

if __name__ == '__main__':
    n = int(input())
    if isUgly(n) :
        print("Ugly Number")
    else : 
        print("Not Ugly Number")