# 69. sqrt(x)

#TC = O(logn)
#SC = O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        h = x

        while l <= h:
            mid = h + (l - h)//2
            mid_sq = (mid*mid)
            if mid_sq == x:
                return mid
            elif mid_sq > x:
                #search left search space
                h = mid - 1
            else:
                #right search space
                l = mid + 1
        return h
    
