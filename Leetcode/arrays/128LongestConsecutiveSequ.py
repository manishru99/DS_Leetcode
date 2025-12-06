# 128. Longest Consecutive Sequence
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        #Better
        #TC = O(nlogn)
        #SC = O(1)
        
        if n == 0:
            return 0
        nums.sort() #O(nlog n)
        lastSmaller = float('-inf')
        cnt = 0
        max_cnt = 1
        for i in range( n):
            if nums[i] - 1 == lastSmaller:
                cnt += 1
                lastSmaller = nums[i]
            #1st cnt for the new subseq
            elif nums[i] != lastSmaller:
                cnt = 1
                lastSmaller = nums[i]
            max_cnt = max(max_cnt, cnt)
        return max_cnt
'''
#Optimized
#TC = O(n) + O(n) = O(2n)
#SC = O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        set1 = set(nums)
        longest = 0
        for x in set1:
            if x - 1 not in set1:
                #Find consecutive nums
                cnt = 1
                #Subseq is valid till consecutive elem exist 
                while x + 1 in set1:
                    cnt += 1
                    x += 1
                longest = max(longest, cnt)
        return longest






