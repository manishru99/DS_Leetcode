# 76. Minimum Window Substring

# Brute
# TC = O(n^2)
# SC = O(256)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        minlen = 1e9
        s_ind = -1
        
        for i in range(len(s)):
            mpp = [0] * 256
            cnt = 0
            for c in t:
                mpp[ord(c)] += 1

            for j in range(i, len(s)):

                if mpp[ord(s[j])] > 0:
                    cnt += 1
                mpp[ord(s[j])] -= 1

                if cnt == len(t):
                    if j - i + 1 < minlen:
                        minlen = j - i + 1
                        s_ind = i
                    break
        if s_ind == -1:
            return ""
        return s[s_ind : s_ind + minlen]

# Sliding window
#TC = O(n+m) SC = O(128)
'''- O(m) to build the frequency map for t.
- The main while r < n loop runs up to n times.
- Inside that, the while cnt == required loop also moves the left pointer forward—but each character enters and exits the window at most once.
- So even though it's two nested loops, each character is processed at most twice (once when r enters and once when l exits), making it O(n).
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If either input string is empty, no window can be formed
        if not t or not s:
            return ""

        n, m = len(s), len(t)               # Lengths of strings s and t
        mpp = [0] * 128                     # ASCII-based frequency map for characters in t
        l, r = 0, 0                         # Sliding window pointers
        minlen = 1e9                        # Stores length of smallest valid window found
        sind = -1                           # Stores starting index of smallest valid window
        cnt = 0                             # Tracks how many required characters have been matched

        # Populate frequency map with counts of characters in t
        for c in t:
            mpp[ord(c)] += 1

        required = sum(mpp)                # Total required matches (including duplicate characters)
        # not comparing with len(t) a it'll give len not sum, we require including the duplicates too

        # Begin sliding window traversal
        while r < n:
            # If current character in s is still needed, increment match counter
            if mpp[ord(s[r])] > 0:
                cnt += 1
            # Consume this character from the map regardless
            mpp[ord(s[r])] -= 1

            # If all required characters have been matched
            while cnt == required:
                # Update minimum window and start ind if current one is shorter
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    sind = l

                # Try to shrink the window from the left
                mpp[ord(s[l])] += 1        # Restore frequency of outgoing character
                if mpp[ord(s[l])] > 0:     # If it's a required character, decrement match counter
                    cnt -= 1
                l += 1                     # Slide window forward

            r += 1                         # Expand window to the right

        # If no valid window was found, return empty string
        if sind == -1:
            return ""

        # Return the minimum window substring found
        return s[sind : sind + minlen]


