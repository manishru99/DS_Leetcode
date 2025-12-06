# 560. Subarray Sum Equals K

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        '''
        #TC = O(n^2)
        #SC = O(1)
        cnt = 0
        for i in range(n):
            sum1 = 0
            for j in range(i, n):
                sum1 += nums[j] #subarr sum
                if sum1 == k:
                    cnt += 1
        return cnt
        '''
        #TC = O(n)
        #SC = O(n)
        mpp = defaultdict(int)
        preSum = 0
        cnt = 0
        mpp[0] = 1 #Setting 0 in the map
        for i in range(n):
            preSum += nums[i]    # Prefix sum
            remove = preSum - k  #s-k
            # Add the number of subarrays to be removed:
            cnt += mpp[remove]
            #Update the map
            mpp[preSum] += 1
        return cnt
