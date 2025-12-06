class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + (high - low) // 2
           

            if nums[mid] >= nums[mid+1]:
                #This ensures that the algorithm doesn’t always prefer moving to the right, 
                #allowing it to stop within the flat region peak on the left
                high = mid
            else:
                #peak on right
                low = mid + 1
        return low

'''
Divide and Conquer: In each step of the binary search, look at the middle element and compare it with its neighbors:

If the middle element is greater than its neighbors, it is a peak.
Otherwise, move to the side where a larger neighbor exists. This is because a peak must exist on that side.
Key Observations:

If nums[mid] > nums[mid + 1], a peak exists on the left side (including mid).
If nums[mid] < nums[mid + 1], a peak exists on the right side.
Why This Works:

The array is implicitly treated as having -∞ at both ends.
By always moving toward a higher neighbor, we ensure convergence to a peak
'''