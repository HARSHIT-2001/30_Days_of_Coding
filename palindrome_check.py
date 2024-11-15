class Palindrome_class:
# Python3 programs to check if a number is Palindrome or not.

    # [1st Approach] Using Number as String – O(N) Time and O(N) Space:
    def isPalindrome(self, x: int) -> bool:
        # Storing the number as a string
        num = str(x)
        
        # Checking the palindrome using String Slicing method 
        if num[::-1] == num:
            return True
        return False
    

    # [2nd Approach] Comparing with reverse of original number – O(N) Time and O(1) Space:
    def check_palindrome(self, n: int) -> bool:
        reverse = 0

        # Copy of the original number 
        temp = n
        while temp != 0:
            reverse = reverse * 10 + temp % 10
            temp = temp // 10

        # If reverse is equal to the original number, the number is palindrome
        return reverse == n
    

    # [3rd Approach] Using Number as String – O(N) Time and O(1) Space:
    def checkPalindrome(self, n) -> bool:
    
        # Run loop from 0 to len/2
        for i in range(0, len(n)//2):
            if n[i] != n[len(n)-i-1]:
                return False
            
        # If the above loop doesn't return then it is palindrome
        return True


# Driver code
n = 12321
obj = Palindrome_class()
print(obj.isPalindrome(n))
print(obj.check_palindrome(n))
print(obj.checkPalindrome(str(n)))

