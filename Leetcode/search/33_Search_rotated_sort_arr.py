# 33. Search in Rotated Sorted Array

# Brute force
'''
simple linear search
TC = O(n)
'''

# Since the arr is already sorted I can think of using Binary search
# As sorted it means we can eliminate portions and reduce TC

'''
First, we identify the sorted half of the array. 
Once found, we determine if the target is located within this sorted half. 
If not, we eliminate that half from further consideration. 
Conversely, if the target does exist in the sorted half, we eliminate the other half.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1

        #
        while(low <= high):
            mid = low + (high-low)//2
            #If target present at mid
            if(nums[mid] == target):
                return mid

            #Find the sorted part and apply logic to 
            #left part sorted
            if(nums[low] <= nums[mid]):
                #If the target exists in the left sorted half
                if(nums[low] <= target and target <= nums[mid]):
                    #eliminate the right part
                    high = mid - 1
                else:
                    #eliminate the left part
                    low = mid + 1
            #Right part is sorted
            else:
                #If the target exists in the right sorted half
                if(nums[mid] <= target and target <= nums[high]):
                    #eliminate the left part
                    low = mid + 1
                else:
                    #eliminate the right part
                    high = mid - 1
        return -1

