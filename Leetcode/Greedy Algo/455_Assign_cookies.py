# Assign Cookies
# TC = O(nlogn + mlogm) + O(n + m) = O(nlogn + mlogm)
# SC = O(1)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g) #g -> greed
        m = len(s) # s -> size of cookie
        g.sort()
        s.sort()
        l = 0 # l is the index of cookie
        r = 0 # r is the index of greed
        while l<m and r<n:
            if g[r] <= s[l]:
                r += 1
            # cookie cannot satisfy the next greed which are higher
            l += 1 
        return r 
