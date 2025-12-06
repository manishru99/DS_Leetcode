# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        #Brute
        #TC = O(n^3)
        #SC = O(1)
        '''
        max_sum = 0
        for i in range(n):
            for j in range(i, n):
                # subarray = arr[i.....j]
                sum1 = 0
                # add all the elements of subarray:
                for k in range(i, j+1):
                    sum1 += nums[k]
                #Update max_sum
                max_sum = max(max_sum, sum1)
        return max_sum
        '''
        #Better
        #TLE error
        #TC = O(n^2)
        #SC = O(1)
        '''
        max_sum = -sys.maxsize - 1
        for i in range(n):
            sum1 = 0
            for j in range(i, n):
                sum1 += nums[j]
                max_sum = max(max_sum, sum1)
        return max_sum
        '''
        #Optimized
        #TC = O(n)
        #SC = O(1)
        #For particular problem as nums=[-1] won't run:
        #So calc maxi before checking sum1 < 0
        sum1 = 0
        maxi = -sys.maxsize - 1
        for i in range(len(nums)):
            sum1 += nums[i]
            # Update maxi
            maxi = max(maxi, sum1)
            # Check sum1
            if sum1 < 0:
                sum1 = 0
        return maxi

