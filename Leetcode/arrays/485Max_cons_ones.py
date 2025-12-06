# 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 0 # as soon as we hit a 0, reset the count
        # if the last element is 1, we might not have updated max_cnt
        return max_cnt
    
#TC = O(n)
#SC = O(1)