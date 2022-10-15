
# Function to print maximum number that can be formed
# using N segments
def printMaxNumber(n):
     
    # If n is odd
    if (n % 2 == 1):
         
        # use 3 three segment to print 7
        print("7",end="");
 
        # remaining to print 1
        for i in range(int((n - 3) / 2)):
            print("1",end="");
 
    # If n is even
    else:
         
        # print n/2 1s.
        for i in range(n/2):
            print("1",end="");
 
# Driver's Code
n = 6;
printMaxNumber(n);
print("")
# This code contributed by Rajput-Ji