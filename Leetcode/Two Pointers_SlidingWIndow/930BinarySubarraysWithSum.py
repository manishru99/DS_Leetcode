# 930. Binary Subarrays With Sum

#TC = O(2 * 2n)
#SC = O(1)

class Solution:
    def less_equal_to_k(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        cnt = 0
        sum1 = 0
        l, r = 0, 0
        #edge case
        if goal < 0: return 0
        while r < n:  #O(n)
            sum1 += nums[r]
            while sum1 > goal:  #O(n)
                sum1 -= nums[l]
                l += 1 #shrink window
            cnt += r - l + 1 # window length
            r += 1  #expand window
        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.less_equal_to_k(nums, goal) - self.less_equal_to_k(nums, goal - 1) # runs 2 times so O(2*2n)
        
        
            
