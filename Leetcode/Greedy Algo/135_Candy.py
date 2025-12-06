# 135 Candy 

# solution 1 (Brute Force)
# TC = O(3n) SC = O(2n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        left[0] = 1
        right[n-1] = 1
        #left
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1
        # right
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                ratings[i] = ratings[i+1] + 1
            else:
                right[i] = 1
        sumi = 0
        for i in range(n):
            sumi = sumi + max(left[i], right[i])
        return sumi

# Solution 2
# TC = O(2n) SC = O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        left[0] = 1
        right[n-1] = 1
        #left
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1
        # right
        curr, right = 1, 1
        sumi = max(1, left[n-1]) # for the last
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                curr = right + 1
                right = curr
            else:
                curr = 1
                right = curr
            sumi += max(left[i], curr)
        return sumi
    
# Solution 3 (Same as sol 2 with proper list initialization)
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        # Step 1: Initialize candy distribution lists
        left = [1] * n
        right = [1] * n

        # Step 2: Left pass - satisfy increasing sequences
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1  # Increase candy count
        
        # Step 3: Right pass - satisfy decreasing sequences
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1  # Increase candy count
        
        # Step 4: Compute the final sum by taking the max of both passes
        return sum(max(left[i], right[i]) for i in range(n)) 
    
# Solution 4 (Optimized on space) Slope Approach Intuition Based
# TC = O(n) SC = O(1)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sumi = 1
        i = 1
        while i < n:
            # flat
            if ratings[i] == ratings[i-1]:
                sumi += 1
                i += 1
                continue
            # increasing slope
            peak = 1
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1 # First increase the peak then add it to the sum
                sumi += peak
                i += 1
            # decreasing slope
            down = 1
            while i < n and ratings[i] < ratings[i-1]:
                sumi += down # add the down slope candies
                down += 1 # increase after starting from 1
                i += 1
            # If down > peak, we need to adjust the candies
            # because we need to ensure that the peak is higher than the down slope
            if down > peak:
                sumi += (down - peak)
        return sumi
