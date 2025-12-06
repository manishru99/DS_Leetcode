#125. Valid Palindrome

#3 appraoches

# Approach 1: Brute force (Rfr Neetcode)
# TC = O(n) SC = O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        revstr = ''
        for c in s:
            if c.isalnum():
                revstr += c.lower()
        return revstr == revstr[::-1]

#Approach 2: Recursive
'''TC = O(n)
- The function performs one comparison per recursive call.
- It continues until the index i reaches len(s) // 2, effectively checking n/2 character pairs.
- Since constants are dropped in Big-O notation, the complexity is O(n) where n is the length of the string.

SC = O(n)
- Because it's recursive, each call adds a frame to the call stack.
- The depth of the recursion is also n/2, which means the space used by the stack grows linearly with the length of the string.
'''
class Solution:
    def isPalindrome(self, s: str, i: int = 0) -> bool:
        # Base case: if the index reaches the middle of the string
        if i >= len(s) // 2:
            return True

        # Check if characters at the current index and its mirror index are the same
        if s[i] != s[len(s) - i - 1]:
            return False

        # Recursive call to check the next pair of characters
        return self.isPalindrome(s, i + 1)
    
# approach 3: Two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            #If s[left] is not alphanumeric, increment left.
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            #Compare left and right for equality 
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

#TC = O(n)
#SC = O(1)