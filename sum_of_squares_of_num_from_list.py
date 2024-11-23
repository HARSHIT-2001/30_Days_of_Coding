# This program calculates the sum of squares of even and odd numbers from a given list and returns the results as a list.
import math

# 1st Approach...
# It has Time complexity of O(n) and Space Complexity of O(1).
def sumsquare(l):
    sum_even = 0
    sum_odd = 0
    sum_list = []
    
    for i in l:
        if (i%2 == 0):
            sum_even += pow(i,2)
            #sum_even += (i**2)
            
        else:
            sum_odd += pow(i,2)
            #sum_even += (i**2)
            
    sum_list.append(sum_odd)
    sum_list.append(sum_even)
    
    return sum_list
    

#2nd Approach (List Comprehension Approach)...
# It has Time complexity of O(n) and Space Complexity of O(n).
def sumsquare(l):
    sum_even = sum([i**2 for i in l if i % 2 == 0])
    sum_odd = sum([i**2 for i in l if i % 2 != 0])
    return [sum_odd, sum_even]


#3rd Approach (Single Pass Optimization)...
# It has Time complexity of O(n) and Space Complexity of O(1).
def sumsquare(l):
    sum_even, sum_odd = 0, 0
    for i in l:
        if i % 2 == 0:
            sum_even += i**2
        else:
            sum_odd += i**2
    return [sum_odd, sum_even]


l = [10,2,30,4,50,6]    
print(sumsquare(l))