# 278. First Bad Version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        bad = 0 # initialize bad as 0 
        while low <= high:
            mid = low + (high - low)//2
            if not isBadVersion(mid):
                # prev version are good
                low = mid + 1
            # is bad check if left part also has bad to find the 1st one
            else:
                bad = mid
                high = mid - 1
        return bad

                
            
# Since 1 <= bad <= n <= 231 - 1
# we can return low 
def firstBadVersion(self, n: int) -> int:
    low, high = 1, n
    while low < high:
        mid = (low + high) // 2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low