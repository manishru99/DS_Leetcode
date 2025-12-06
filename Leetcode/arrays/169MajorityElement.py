# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        #MLE error
        '''
        max_num = max(nums)
        mpp = [0] * (max_num + 1)
        for num in nums:
            mpp[num] += 1
            if mpp[num] > n/2:
                return num
        return -1
        '''
        #TC = O(n) + O(n)
        #SC = O(n) (for dict)
        '''
        mpp = {}
        for num in nums:
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1

        # Searching for the majority element
        for key, val in mpp.items():
            if val > (n/2):
                return key
        return -1
        '''
        #Optimized
        #Moore’s Voting Algorithm

        #TC = O(n) + O(n)
        #SC = O(1)
        cnt = 0
        ele = 0
        for i in range(n):
            if cnt == 0:
                cnt = 1
                ele = nums[i]
            elif nums[i] == ele:
                cnt += 1
            else:
                cnt -= 1

        cnt1 = 0
        for i in range(n):
            if nums[i] == ele:
                cnt1 += 1
        
        if cnt1 > n/2:
            return ele
        return -1


                


