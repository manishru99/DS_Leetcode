# 213. House Robber II

# Memoization
# TC = O(2n) = O(n) Recursive calls for ans1 and ans2
# SC = O(n) + O(n) = O(n) recursive stack + n combined size for dp1 and dp2
# - nums[:x] gives all elements up to index x (exclusive).
#- nums[:-1] means all elements except the last one.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def f(ind, arr, dp):
            # Base case: no houses left to rob
            if ind >= len(arr):
                return 0
            if dp[ind] != -1:
                return dp[ind]
            
            # Option 1: rob current house and skip next
            take = arr[ind] + f(ind + 2, arr, dp)
            
            # Option 2: skip current house
            not_take = f(ind + 1, arr, dp)

            dp[ind] = max(take, not_take)
            return dp[ind]

        # Exclude first house
        temp1 = nums[1:]
        dp1 = [-1] * len(temp1)

        # Exclude last house
        temp2 = nums[:-1]
        dp2 = [-1] * len(temp2)

        ans1 = f(0, temp1, dp1)
        ans2 = f(0, temp2, dp2)

        return max(ans1, ans2)

# Tabulation sol 1
'''
TC = O(n) - The problem is solved by considering two linear robbery scenarios:
- Robbing houses from index 1 to n−1 (excluding the first)
- Robbing houses from index 0 to n−2 (excluding the last)
- Each for loop iterates through up to n − 1 elements
SC = O(n)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        # exclude 1st house
        temp1 = nums[1:]
        dp1 = [0] * len(temp1)
        dp1[0] = temp1[0]
        if len(temp1) > 1:
            dp1[1] = max(temp1[0], temp1[1])

        # exclude last house
        temp2 = nums[:-1]
        dp2 = [0] * len(temp2)
        dp2[0] = temp2[0]
        if len(temp2) > 1:
            dp2[1] = max(temp2[0], temp2[1])

        for i in range(2, len(temp1)):
            not_take = 0 + dp1[i - 1]
            take = temp1[i] + dp1[i - 2]
            dp1[i] = max(not_take, take)
        
        for i in range(2, len(temp2)):
            not_take = 0 + dp2[i - 1]
            take = temp2[i] + dp2[i - 2]
            dp2[i] = max(not_take, take)
        
        return max(dp1[-1], dp2[-1])
    
# Tabulation sol 2 (readable)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def solve(arr):
            m = len(arr)
            if m == 0:
                return 0
            if m == 1:
                return arr[0]

            dp = [0] * m
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, m):
                # Either skip current house or rob it and skip previous
                dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
            return dp[m - 1]

        # Case 1: Rob houses from index 1 to n-1 (exclude first)
        ans1 = solve(nums[1:])
        # Case 2: Rob houses from index 0 to n-2 (exclude last)
        ans2 = solve(nums[:-1])

        return max(ans1, ans2)


# Space Optimization
# TC = O(n) + O(n) for running 2 loops
# SC = O(1)
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Given a list of house values, determines the maximum amount of money that can be robbed 
        without robbing adjacent houses (houses are arranged in a circular pattern).

        Args:
        nums (List[int]): A list representing the amount of money available in each house.

        Returns:
        int: Maximum amount that can be robbed.
        """

        n = len(nums)

        # Edge Case: If there is only one house, return its value directly.
        if n == 1:
            return nums[0]

        temp1, temp2 = [], []  # Two arrays to handle the circular condition

        def f(arr, n):
            """
            Computes the maximum money that can be robbed for a linear set of houses 
            (ignoring circular adjacency constraints).

            Args:
            arr (List[int]): Subset of house values to process.
            n (int): Size of the original house list.

            Returns:
            int: Maximum amount that can be robbed from this subset.
            """

            n1 = len(arr) # len changes now from the original array
            prev = arr[0]  # Stores max amount stolen from previous step
            prev2 = 0  # Stores max amount stolen from two steps before

            for i in range(1, n1):
                # Case 1: Rob current house (`pick`)
                pick = arr[i]
                if i > 1:
                    pick += prev2  # Add value from house two steps before
                
                # Case 2: Skip current house (`not_pick`)
                not_pick = prev  # Retain previous max amount

                # Choose the maximum amount possible at the current step
                curi = max(pick, not_pick)

                # Update `prev` and `prev2` for next iteration
                prev2 = prev
                prev = curi

            return prev

        # Step 1: Create two separate arrays handling circular adjacency:
        # - `temp1`: Excludes the first house
        # - `temp2`: Excludes the last house
        for i in range(0, n):
            if i != 0:
                temp1.append(nums[i])  # Houses excluding the first
            if i != n - 1:
                temp2.append(nums[i])  # Houses excluding the last

        # Step 2: Compute the max money possible for both cases
        ans1 = f(temp1, n)  # Case 1: Ignore first house
        ans2 = f(temp2, n)  # Case 2: Ignore last house

        # Step 3: Return the maximum of both cases
        return max(ans1, ans2)