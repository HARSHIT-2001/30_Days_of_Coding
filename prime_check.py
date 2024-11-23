# This program takes an integer as input and prints out all the possible prime between 1 and your number.
# It has Time Complexity of O(n ** 1.5) or O(n to the power of 1.5), and Space complexity of O(1). 

def is_prime(numb):
    for i in range(2, int(numb**0.5)+1):
        if (numb % i == 0) and numb!=i:
            return False
        
    else:
        return True


def prime_num(num):
    print("This is the list of numbers between 1 and ", num, " prime numbers: \n")

    for i in range(2,num):
        if (is_prime(i)):
            print(i, end = ' ')
    
            

# Driver Code
input_num = int(input("Enter your Number-> ")) 
prime_num(input_num)    # Taking input by user.