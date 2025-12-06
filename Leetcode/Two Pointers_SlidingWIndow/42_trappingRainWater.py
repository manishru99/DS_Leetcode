# Solution 4: Two pointers approach
# TC = O(n) SC = O(1)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)              # Total number of bars
        l, r = 0, n - 1              # Initialize two pointers: left (l) and right (r)
        lMax, rMax = 0, 0            # Track max height seen from left and right
        total = 0                    # Accumulator for total trapped water

        while l <= r:
            # Compare heights at both ends to decide which side to process
            if height[l] <= height[r]:
                # If current left bar is lower than right bar
                if lMax > height[l]:
                    # Water can be trapped at l (bounded by lMax)
                    total += lMax - height[l]
                else:
                    # Update lMax as new highest from left
                    lMax = height[l]
                l += 1                # Move left pointer inward
            else:
                # If current right bar is lower than left bar
                if rMax > height[r]:
                    # Water can be trapped at r (bounded by rMax)
                    total += rMax - height[r]
                else:
                    # Update rMax as new highest from right
                    rMax = height[r]
                r -= 1                # Move right pointer inward

        return total                  # Return the total trapped water


class Solution:
    '''
    # Solution 3: Same as solution 2
    def find_left_max(self, height):
        #Find prefix Max
        prefix_max_arr = []
        current_max = float('-inf')
        for num in height:                        #O(n)
            current_max = max(current_max, num)
            prefix_max_arr.append(current_max)
        return prefix_max_arr

    def find_right_max(self, height):
        suffix_max_arr = []
        current_max = float('-inf')
        for num in reversed(height):          #O(n)
            #Update current max
            current_max = max(current_max, num)
            suffix_max_arr.append(current_max)
        suffix_max_arr.reverse()
        return suffix_max_arr

    def trap(self, height: List[int]) -> int:
        total = 0 #Total water trapped
        left_max_arr = self.find_left_max(height)
        right_max_arr = self.find_right_max(height)
        for i in range(len(height)):               #O(n)
            if height[i] < left_max_arr[i] and height[i] < right_max_arr[i]:
                total += min(left_max_arr[i], right_max_arr[i]) - height[i]
        return total
    '''


#TC = O(n)

#Solution 1 - Brute Force
#For each element, find the maximum level of water it can trap after the rain, 
# which is equal to the minimum of maximum height of bars on both the sides minus its own height.
# TC = O(n^2)
# SC = O(1)
'''
def trap(self, height: List[int]) -> int:
    n = len(height)
    waterTrapped = 0
    for i in range(n): #O(n)
        j = i
        leftMax, rightMax = 0, 0
        # FInd leftMax
        while j >= 0: #O(i)
            leftMax = max(leftMax, height[j])
            j -= 1
        # FInd rightMax
        j = i
        while j < n: #O(n-i)
            rightMax = max(rightMax, height[j])
            j += 1
        # Note: for the max height building, itself will be the leftMax and rightMax
        waterTrapped += min(leftMax, rightMax) - height[i]
    return waterTrapped
    '''

# Solution 2 - By using prefix and suffix arrays and precompute the leftMax and rightMax at each index
# TC = O(3n) = O(n)
# SC = O(2n) = O(n) # For prefix and suffix arrays
'''
def trap(self, height: List[int]) -> int:
    n = len(height)
    prefix = [0] * n
    suffix = [0] * n
    # Fill prefix arr
    prefix[0] = height[0]
    for i in range(1, n):
        prefix[i] = max(prefix[i-1], height[i])
    # Fill suffix arr
    suffix[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        suffix[i] = max(suffix[i+1], height[i])
    waterTrapped = 0
    for i in range(n):
        waterTrapped += min(prefix[i], suffix[i]) - height[i]
    return waterTrapped
'''