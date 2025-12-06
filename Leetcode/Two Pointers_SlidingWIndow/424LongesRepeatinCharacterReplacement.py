# 424. Longest Repeating Character Replacement

# Solution 1 Brute force
#TC = O(n^2)
#SC = O(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        #Generate all possible substr
        maxlen = 0
        for i in range(n):
            hash_map = [0] * 26
            max_freq = 0
            for j in range(i, n):
                #Update freq in hashmap
                hash_map[ord(s[j]) - ord('A')] += 1
                # maxfreq is max of prev maxfreq and current hash 
                max_freq = max(max_freq, hash_map[ord(s[i]) - ord('A')])

                changes = (j - i + 1) - max_freq
                if changes <= k:
                    maxlen = max(maxlen, j-i+1)
                else:
                    break
        return maxlen 

# Solution 2 Brute (same as sol 1) Neetcode
# TC = O(n^2) SC = O(m) Where 
#n is the length of the string and m is the total number of unique characters in the string.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        for i in range(len(s)):
            hashmap = {}
            maxf = 0
            for j in range(i, len(s)):
                hashmap[s[j]] = 1 + hashmap.get(s[j], 0)
                maxf = max(maxf, hashmap[s[j]])
                changes = j - i + 1 - maxf
                if changes <= k:
                    maxlen = max(maxlen, j - i + 1)
                else:
                    break
        return maxlen
'''hashmap.get(s[j], 0) - Tries to retrieve the value associated with key s[j] in the dictionary count.
- If s[j] exists, you get its value (like number of times it’s appeared so far).
- If s[j] doesn’t exist, .get() returns the default value, which in this case is 0.
'''

# Solution 3 Better    
#TC = O(n) + O(n) + O(26)
        #SC = O(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxlen = 0
        maxf = 0
        hash1 = [0]*26
        while r < len(s):   #O(n)
            hash1[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, hash1[ord(s[r]) - ord('A')])
            #If not valid then trim it down
            #If valid then this loop wouldn't exec
            while (r-l+1) - maxf > k:      #O(n)
                # update the hash
                hash1[ord(s[l]) - ord('A')] -= 1
                # maxf will ch
                maxf = 0
                #Now select new maxf from the hashmap
                for i in range(26):     #O(26)
                    maxf = max(maxf, hash1[ord(i)])
                # increment l
                l += 1
                
            #See if substr is valid (changes less than eq to k)
            #Redundant below condition
            if (r-l+1) - maxf <= k:
                maxlen = max(maxlen, r-l+1)
            #Or for abv line
            #maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen
    
# Solution 4 same as sol 3 but better one
# TC = O(n) SC = O(26)
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxlen = 0
        maxf = 0
        count = defaultdict(int)  # Dictionary to store character frequencies
        for r in range(len(s)):
            count[s[r]] += 1
            # or if using plain dictionary for hashmap like count = {}, then
            # count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])  # Track the frequency of the most common char

            # If number of changes exceeds k, shrink the window
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # Update the max length of valid window
            maxlen = max(maxlen, r - l + 1)
        return maxlen
        

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Optimized
        #TC = O(n)
        #SC = O(26)
        while r < n:
            hash1[ord(s[r]) - ord('A')] += 1 #Update hashtable
            maxf = max(maxf, hash1[ord(s[r]) - ord('A')])

            #For optimization don't trim down
            if (r-l+1) - maxf > k:
                hash1[ord(s[l]) - ord('A')] -= 1
                maxf = 0
                l += 1

            #changes less than eq to k
            if (r-l+1) - maxf <= k:
                maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen


                


