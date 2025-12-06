# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #eg. nums = [1,2,3]
        n = len(nums) 

        #Recursive sol
        #TC = O(2^n)
        #SC = O(n*2^n)
        #Pick or do not pick
        ans = []
        curr = []
        def powerSet(nums, index, curr):
            if index == n:
                ans.append(curr)
                return
            #Pick
            powerSet(nums, index+1, curr + [nums[index]])
            #Not pick
            powerSet(nums, index+1, curr)
        
        powerSet(nums, 0, [])
        return ans



        




        