import math 
#Importing libraries

class Solution:
    def printSubsequences(self, arr) :
        n = len(arr)
        subsequences = [] 

        # Number of subsequences is (2**n - 1)
        opsize = math.pow(2, n)

        # Run from counter 000..1 to 111..1
        for counter in range(1, int(opsize)):
            subsequence = []  
            for j in range(0, n):
                # Check if jth bit in the counter is set
                # If set, include jth element in the subsequence.
                if counter & (1 << j):
                    subsequence.append(arr[j])
            subsequences.append(subsequence)  
        return subsequences


    def sum_arr(self, arr):
        # Storing sum of elements of array in sum_ttl 
        sum_ttl = 0

        # Adding all the elements to calculate sum of array.
        for i in arr:
            sum_ttl += i
        return sum_ttl


    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Creating all the subarrays in ab_arr
        ab_arr = self.printSubsequences(nums)
        print(ab_arr)
        res = -1
    
        # Iterating through subarrays to find sum equls to k
        for i in ab_arr:
            total = self.sum_arr(i)
            
            if k == total :
                res = len(i)
                return res
            
        return res
