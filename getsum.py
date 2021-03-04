# Python3 program to find the smallest
# number whose sum of digits is also N

# Function to get sum of digits
def getSum(n):

    sum1 = 0;
    while (n != 0):
        sum1 = sum1 + n % 10;
        n = n // 10;
    
    return sum1;

# Function to find the smallest
# number whose sum of digits is also N
def smallestNumber(N):

    i = 1;
    while (1):
        # Checking if number has
        # sum of digits = N
        if (getSum(i) == N):
            print(i);
            break;
        
        i += 1;
    
# Driver code
N = int(input('n = '));
smallestNumber(N);

# This code is contributed by Code_Mech
