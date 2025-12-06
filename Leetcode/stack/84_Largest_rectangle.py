# 84. Largest Rectangle in Histogram

# Brute
# TC = O(n^2) SC = O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            height = heights[i]

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1
            
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1
            
            rightMost -= 1
            leftMost += 1
            maxArea = max(maxArea, height * (rightMost - leftMost + 1))
        return maxArea
    
# Using stack
'''
Time Complexity: O( N ) + O (N)
Space Complexity: O(N)
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = [] # Stack to store indices of increasing bar heights
        max_area = 0
        for i in range(n):
            # While the current bar is lower than the bar at the top of the stack
            while st and heights[st[-1]] > heights[i]:
                elem = st[-1]  # Index of the height that is being processed
                st.pop()
                # Next Smaller Element to the right is at index i
                nse = i  
                # Previous Smaller Element is top of the stack after popping
                pse = st[-1] if st else -1 
                # Width is distance between NSE and PSE, exclusive
                # width = nse - pse - 1
                max_area = max(heights[elem] * (nse - pse - 1), max_area)
            st.append(i) # Push current bar index to stack

        # if st is not empty yet
        while st:
            nse = n  # For remaining bars, NSE is beyond the array
            elem = st[-1]
            st.pop()
            pse = st[-1] if st else -1
            max_area = max(heights[elem] * (nse - pse - 1), max_area)
        return max_area

                
                