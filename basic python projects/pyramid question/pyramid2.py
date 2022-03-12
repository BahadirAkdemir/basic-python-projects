# Question wants me to treat the input as pyramid. So I have to use 2d array.
# Question does not say that the numbers won't be negative. So I could not change the prime numbers to -1 or any number.
# Since I cannot change the prime numbers to -1, I have to use a temporary array to store the original values.


#modules
import math
import copy


def isPrime(number):

    """
    Checks if the number is prime or not.
    """

    if number<2:
        return False

    n = int(math.sqrt(number))

    for i in range(2,n+1):
        if number%i==0:
            return False

    return True


def find_max_sum(pyramid):

    temp_pyramid = copy.deepcopy(pyramid) #Copy the original array to a temporary array

    """
    Find the maximum sum of a path in a pyramid.
    """

    if isPrime(pyramid[0][0]): # If array has one element and it is prime, then the sum will be zero.
        pyramid[0][0]=0
        return pyramid[0][0]

    if len(pyramid) == 1: # If array has one element, then the sum is this element
        return pyramid[0][0]


    for i in range(len(pyramid) - 1, 0, -1):

        for j in range(0,len(pyramid[i])-(len(pyramid)-i)):

            if(isPrime(pyramid[i-1][j])): # If the number is prime, then the sum will be not included because it is not in the way.
                continue
            else:
                available_choices=[]
                if (j-1) >= 0: 
                    if not isPrime(pyramid[i][j-1]) or not temp_pyramid[i][j-1]==pyramid[i][j-1]:
                        available_choices.append(pyramid[i][j-1])

                if not isPrime(pyramid[i][j+1]) or not temp_pyramid[i][j+1]==pyramid[i][j+1]:
                    available_choices.append(pyramid[i][j+1])
                
                if not isPrime(pyramid[i][j]) or not temp_pyramid[i][j]==pyramid[i][j]:
                    
                    available_choices.append(pyramid[i][j])

                if not len(available_choices)==0:
                    pyramid[i-1][j] += max(available_choices)


    return pyramid[0][0] # The sum of the first row is the maximum sum (dynamic programming).
    

def get_input(path):

    """
    Reads the input from the file and returns the pyramid as a 2d array.
    """

    with open(path) as f:
        number_of_lines = len(f.readlines()) #Find the number of lines in the file in order to measure the height of the pyramid and create n x n  2d array
    
        pyramid_array = [[0 for i in range(0,number_of_lines)] for i in range(0, number_of_lines)] # n x n 2d array with zeros
        f.seek(0) #Reset the pointer
        r=f.read() #Read the file

    r=r.split("\n") #Split the file according to the lines

    for i in range(len(r)):
        r[i]=r[i].split(" ") #Split the lines according to the spaces

    for i in range(0,len(r)):
        for j in range(0,len(r[i])):
            pyramid_array[i][j]=int(r[i][j]) #Fill the 2d array with the values from the file
    return pyramid_array


pyramid = get_input("pyramid question/input.txt")


print(find_max_sum(pyramid))



