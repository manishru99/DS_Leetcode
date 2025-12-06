class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        str1 = str(x)
        return str1 == str1[::-1]
        '''
        #TC = O(log n)
        #SC = O(1)
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        y = 0
        #construct the half from reverse
        while y < x:
            y = y*10 + (x % 10)
            x //= 10
        #Finally, we check if the original number is equal to the reversed half or if it matches when the last digit of the reversed half is removed (for odd-length numbers).
        return x == y or x == y//10
