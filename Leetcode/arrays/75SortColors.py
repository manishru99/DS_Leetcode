# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Hint 2
        #TC = O(n) + O(n)
        #SC = O(1)
        '''
        cnt0, cnt1, cnt2 = 0, 0, 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                cnt0 += 1
            elif nums[i] == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt0, cnt0+cnt1):
            nums[i] = 1
        for i in range(cnt0 + cnt1, n):
            nums[i] = 2
        #ANother approach for copying elem back to arr
        for i in range(n):
        if i < cnt0:
            nums[i] = 0
        elif i < cnt0 + cnt1:
            nums[i] = 1
        else:
            nums[i] = 2
        '''

        #Dutch National Flag algo
        #TC = O(n)
        #SC = O(1)
        n = len(nums)
        low, mid = 0, 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  #arr[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


