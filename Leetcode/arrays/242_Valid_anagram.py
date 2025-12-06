# 242. Valid Anagram

# TC = O(m+n) m len(s), n len(t)
# SC = O(1) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        cntS, cntT = {}, {}
        for i in range(len(s)):
            # at key=s[i] increment the val by 1
            # cntS[s[i]] will give error if s[i] doesn't exist in cntS
            # default return 0
            cntS[s[i]] = 1 + cntS.get(s[i], 0)
            cntT[t[i]] = 1 + cntT.get(t[i], 0)
        return cntS == cntT
    
# Follow up: What if the inputs contain Unicode characters? 
# How would you adapt your solution to such a case?

## TC = O(m+n) m len(s), n len(t)
# SC = O(1) 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for val in count:
            if val != 0: return False
        return True
    
'''
This is a clever way to map a lowercase letter (a to z) to an index from 0 to 25 so you can use it in a fixed-size list, like a frequency counter.
- s[i]: the i-th character of the string s.
- ord(s[i]): gets the Unicode code point of that character. For example, ord('c') → 99.
- ord('a'): code point of 'a', which is 97.
- So, ord(s[i]) - ord('a') shifts the letter's Unicode so that:
- 'a' → 0
- 'b' → 1
- 'z' → 25
This lets you use a list like count = [0] * 26 where:
- count[0] tracks the number of 'a's,
- count[1] tracks 'b's, and so on.

'''