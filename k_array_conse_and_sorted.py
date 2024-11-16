'''
Suppose You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
    Its maximum element if all of its elements are consecutive and sorted in ascending order.
    -1 otherwise.

You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)]. 

Input: nums = [1,2,3,4,3,2,5], k = 3

Output: [3,4,-1,-1,-1]

Explanation:
There are 5 subarrays of nums of size 3:

[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive. '''

class Solution:
    def are_consecutive(self, arr):
        n = len(arr)
        _sum = 0
        min_val = arr[0]
        max_val = arr[0]

        for i in range(n):
            _sum += arr[i]
            if arr[i] < min_val:
                min_val = arr[i]
            if arr[i] > max_val:
                max_val = arr[i]

        if _sum == (n * (min_val + max_val)) / 2 and max_val - min_val == n - 1:
            return True
        else:
            return False

    def all_elements_same(self, arr):
        return all(x == arr[0] for x in arr)
    
    def sorted_or_not(self, arr):
        s_arr = arr[::]
        arr = sorted(arr)
    
        if arr != s_arr :
            return False
        return True

    def resultsArray(self, nums , k):
            Pow_arr = []
            count = 0
            n = len(nums)
            

            for i in range(n-k+1):
                temp_arr = []
                for j in range(i,i+k):
                    temp_arr.append(nums[j])

                Pow_arr.append(temp_arr)
                
            # x = 
            return_arr = [-1]* len(Pow_arr)
    
            for i in Pow_arr:
                if len(i) == 1:
                    return_arr[count] = i[-1]
                    
                elif self.all_elements_same(i):
                    return_arr[count] = -1
                    
                elif self.are_consecutive(i):
                    if self.sorted_or_not(i):
                        return_arr[count] = i[-1]

                count+=1
            return return_arr
    

# Driver program to test above function
def main():
    # Input 1
    nums = [1,2,3,4,3,2,5]
    k = 3  
    sol = Solution()
    print(sol.resultsArray(nums,k))

    # Input 2
    nums = [2,2,2,2,2]
    k = 4
    sol = Solution()
    print(sol.resultsArray(nums,k))

    
if __name__ == "__main__":
    main()
    