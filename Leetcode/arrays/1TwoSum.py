# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        #Brute
        #TC = O(n^2)
        #SC = O(1)
        '''
        sum1 = 0
        for i in range(n-1):
            for j in range(i+1, n):
                sum1 = nums[i] + nums[j]
                if sum1 == target:
                    return [i, j]
        return 0
        '''
        #Better (using hashing) Rfr Neetcode
        #searching in a hashmap takes O(1) generally
        # Here hashmap stores the index of the elem
        #TC = O(n)
        #SC = O(n)
        '''
        mpp = {}
        for i in range(n):
            num = nums[i]
            diff = target - num
            #try to find if target - num is present in the map or not.
            if diff in mpp:
                return [i, mpp[diff]]
            #Store index of num
            mpp[num] = i
        return [-1, -1]
        '''

        # Optimized (2 pointers)
        #THis will work for sorted nums array
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            sum1 = nums[left] + nums[right]
            if sum1 == target:
                return [left, right]
            elif sum1 < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
        '''
        
        #For unsorted arr
        #TC = O(n) + O(N*logN)
        #SC = O(n) due to storing the indexed list.
        #This code keeps track of the original indices by pairing each 
        # number with its index before sorting. This way, when we find 
        # the pair that sums to the target, we can return their original indices.
        indexed_arr = [(num, i) for i, num in enumerate(nums)] #list of tuples (nums, index)
        # or use [[num, i] for i, num in enumerate(nums)]
        indexed_arr.sort()
        left, right = 0, len(indexed_arr) - 1
        while left < right:
            sum1 = indexed_arr[left][0] + indexed_arr[right][0]
            if sum1 == target:
                return [indexed_arr[left][1], indexed_arr[right][1]]
            elif sum1 < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

'''
In Python's enumerate(), the standard order of iteration is (index, value), meaning:
for i, num in enumerate(nums):

- i represents the index of the element in nums.
- num represents the value at that index.
So when constructing indexed_arr, the correct order should be:
indexed_arr = [(num, i) for i, num in enumerate(nums)]

This ensures that each tuple stores (number, index), which is important because 
the numbers will be sorted later, but their original indices must be preserved for the final output.
'''