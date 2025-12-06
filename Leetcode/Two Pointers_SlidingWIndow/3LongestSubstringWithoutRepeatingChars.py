#3. Longest Substring Without Repeating Characters
#Explanation in Leetcode coding doubts 2

#Substring: A substring is a contiguous non-empty sequence of characters within a string.
#Subsequence: A subsequence is a sequence that can be derived from another sequence of elements 
# without changing the order of the remaining elements.

'''
#Solution 1: naive
def lengthOfLongestSubstring(self, s: str) -> int:
        
        #TC = O(n)*O(n)*O(n+n) = O(n^3)
        n = len(s)
        #sub_str = []
        maxLen = 0
        #generate all possible substr and check if unique
        for i in range(n):  #O(n)
            for j in range(i, n):  #O(n)
                #sub_str.append(s[i : j+1])
                sub_str = s[i : j+1]  #O(n)
                
                if len(sub_str) == len(set(sub_str)): #O(n)
                    maxLen = max(maxLen, len(sub_str))
        return maxLen

# Solution 2:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Better solution (accepted)
        #TC = O(n^3)
        #SC = O(n)
        n = len(s)
        maxLen = 0
        #generate all possible substr and check if unique
        for i in range(n):  #O(n)
            seen_chars = set()
            #unique = True
            for j in range(i, n):  #O(n)
                if s[j] in seen_chars:
                    #unique = False
                    #break if seen
                    break
                #Add if not seen before
                seen_chars.add(s[j])
                sub_str = s[i : j+1]  #O(n)
                #checks if the length of the substring is equal to the number of unique characters in it. 
                # If they are equal, it means that all characters in sub_str are unique.
                if len(sub_str) == len(set(sub_str)): #O(n)
                    maxLen = max(maxLen, len(sub_str))
        return maxLen
'''
    

# Solution 3 Brute  (Easy sol)
# TC = O(n*m) SC = O(m)
# Where n is the length of the string and m is the total number
#  of unique characters in the string.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charset = set()
            # Edge case: j starts from i itself
            for j in range(i, len(s)):
                if s[j] in charset: 
                    break    
                charset.add(s[j])
            res = max(res, len(charset))
        return res
'''Explanation for edge case: In your current implementation, you 
start checking substrings from index i and loop j from i + 1, which 
excludes the character at index i itself from the charset. So when the 
input is a single space " ", your inner loop never adds any character, 
and len(charset) stays at 0, even though there's one valid character.
'''
                

# Solution 4 Optimized (Neetcode)
# TC = O(n) SC = O(m)
# Note remember to check for a valid substr too
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charset = set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        return res
                


        