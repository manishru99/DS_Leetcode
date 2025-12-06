# 1574. Shortest Subarray to be Removed to Make Array Sorted

from typing import List

# TC = O(n) Each pointer (l, r, l1, r1) iterates through the array at most once.
# SC = O(1) The function operates entirely in-place using only a few integer variables.

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        Given an integer array arr, the goal is to remove the shortest contiguous subarray
        such that the remaining elements are non-decreasing.

        Args:
        arr (List[int]): Input array

        Returns:
        int: Length of the shortest subarray to remove
        """

        # Step 1: Initialize variables
        n = len(arr)
        l, r = 0, n - 1  # l starts at the left, r starts at the right

        # Step 2: Find the longest non-decreasing prefix from the left
        while l + 1 < n and arr[l] <= arr[l + 1]:  
            l += 1  

        # Step 3: Find the longest non-decreasing suffix from the right
        while r - 1 >= 0 and arr[r - 1] <= arr[r]:  
            r -= 1  

        # If the entire array is already non-decreasing, no removal is needed
        if l >= r:  
            return 0  

        # Step 4: Initial assumption - Remove everything from index 0 to r
        ans = r  

        # Step 5: Try merging the prefix and suffix optimally
        l1 = 0  # Left pointer for merging
        r1 = r  # Right pointer for merging
        
        while l1 <= l:  
            # Move r1 forward until we find a position where arr[r1] >= arr[l1]
            while r1 < n and arr[r1] < arr[l1]:  
                r1 += 1  
            
            # Calculate the minimum subarray length to remove
            ans = min(ans, r1 - l1 - 1)  
            l1 += 1  

        return ans  # Return the shortest subarray length to remove