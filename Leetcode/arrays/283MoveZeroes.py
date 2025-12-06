from collections import deque
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        #Brute
        #TC = O(2n)
        #SC = O(x) = O(n) worst case with no 0
        '''
        temp = []
        for i in range(n):  #O(n)
            if nums[i] != 0:
                temp.append(nums[i])
        t_size = len(temp)     #O(x) x is t_size
        for i in range(t_size):
            nums[i] = temp[i]
        for i in range(t_size, n):  #O(n-x)
            nums[i] = 0
        '''
        #Optimized
        '''
        #For my approach I start j from 1st till it finds 1st 0
        #eg. for nums=[1,2,0,4] j and i will swap with itself till 3nd pos 
        '''
        #TC = O(n)
        #SC = O(1)
        i, j = 0, 0
        while i < n:
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            i += 1

# Optimized 2
# TC = O(n) SC = O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = -1
        for i in range(n): # find 1st 0
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return nums
        for k in range(j + 1, n):
            if nums[k] != 0:
                nums[k], nums[j] = nums[j], nums[k]
                j += 1
        return nums
        
        
        