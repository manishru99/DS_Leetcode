# 88. Merge Sorted Array
'''
- Time Complexity: O(m + n) (processing each element once).
- Space Complexity: O(m + n) (due to the extra array nums3).
'''
# Solution 1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = [0] * (m+n)
        l, r = 0, 0
        index = 0
        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                nums3[index] = nums1[l]
                l += 1
            else:
                nums3[index] = nums2[r]
                r += 1
            index += 1
        while l < m:
            nums3[index] = nums1[l]
            l += 1
            index += 1
        while r < n:
            nums3[index] = nums2[r]
            r += 1
            index += 1
        '''
        for i in range(m+n):
            if i < m:
                nums1[i] = nums3[i]
            else:
                nums2[i-n] = nums3[i]
        '''
        nums1[:] = nums3

# SOlution 2 (Doesn't work for leetcode as we have 0 0 0)
# But correct striver solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m-1
        r = 0
        while l >= 0 and r < n:
            if nums1[l] > nums2[r]:
                nums1[l], nums2[r] = nums2[r], nums1[l]
                l -= 1
                r += 1
            else:
                break
        nums1.sort()
        nums2.sort()

# SOlution 3 (Doesn't work for leetcode as we have 0 0 0)
# But correct striver solution)
# TC = O(log2(m + n)) x O(m + n)
# SC = O(1)
from typing import List

class Solution:
    def swap(self, nums1, nums2, ind1, ind2):
        """Swaps elements between nums1 and nums2 if they are out of order."""
        if nums1[ind1] > nums2[ind2]:
            nums1[ind1], nums2[ind2] = nums2[ind2], nums1[ind1]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges sorted arrays nums1 and nums2 in-place using the Shell Sort gap method.
        nums1 contains extra space at the end to accommodate nums2.
        """
        size = m + n  # Total number of elements after merging
        gap = (size // 2) + (size % 2)  # Initial gap for Shell Sort (ceil division)

        while gap > 0:
            l = 0
            r = l + gap

            while r < size:
                # Case 1: Comparing elements between nums1 and nums2
                if l < m and r >= m:
                    self.swap(nums1, nums2, l, r - m)
                # Case 2: Comparing elements inside nums2
                elif l >= m:
                    self.swap(nums2, nums2, l - m, r - m)
                # Case 3: Comparing elements inside nums1
                else:
                    self.swap(nums1, nums1, l, r)

                # Move pointers forward
                l += 1
                r += 1

            # If gap becomes 1, we terminate the loop
            if gap == 1:
                break

            # Reduce gap size for the next iteration (ceil division)
            gap = (gap // 2) + (gap % 2)


            
                    
