# Minimum Platforms (GFG)

# Brute force
# TC = O(n^2) SC = O(1)
class Solution:
    # Function to find the minimum number of platforms required at the railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        # Calculate the number of trains (or intervals)
        n = len(arr)
        # Initialize the minimum number of platforms required as 1 (since at least one platform is needed for the first train)
        mincnt = 1
        # Outer loop to iterate through each train and calculate overlaps
        for i in range(n):
            # Initialize a counter for platforms required for the current train
            cnt = 1
            # Inner loop to check overlaps with all other trains
            for j in range(i + 1, n):
                # Check if the current train (i) overlaps with another train (j)
                # Two conditions to check overlap: (Or 4 conditions on strivers)
                # 1. Train i starts during Train j's time interval (arr[j] <= arr[i] <= dep[j])
                # 2. Train j starts during Train i's time interval (arr[i] <= arr[j] <= dep[i])
                if (arr[i] >= arr[j] and arr[i] <= dep[j]) or (arr[j] >= arr[i] and arr[j] <= dep[i]):
                    # If overlapping, increment the count for the current train
                    cnt += 1
            
            # Update the minimum platforms required with the maximum count found
            mincnt = max(mincnt, cnt)
        # Return the final result: minimum platforms required
        return mincnt

# Optimized (Greedy)
# TC = O(2nlogn) + O(n) = O(nlogn)
# SC = O(1)
class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        # Sort both arrival and departure times
        arr.sort()
        dep.sort()
        
        # Initialize variables
        platforms_needed = 1  # Minimum one platform is required
        max_platforms = 1  # To store the result
        i, j = 1, 0  # Pointers for arrival and departure times
        n = len(arr)
        
        # Iterate over trains
        while i < n and j < n:
            # If a train arrives before the current train departs
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
            else:
                # Train departs, so one platform is freed
                platforms_needed -= 1
                j += 1
            
            # Update the maximum number of platforms needed
            max_platforms = max(max_platforms, platforms_needed)
        
        return max_platforms