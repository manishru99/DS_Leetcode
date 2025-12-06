# 2035. Partition Array Into Two Arrays to Minimize Sum Difference

# Recursion
def subsetSumRecursive(ind, target, arr):
    # Base case: target achieved
    if target == 0:
        return True
    # Base case: only one element to consider
    if ind == 0:
        return arr[0] == target

    # Recursive case: exclude or include current element
    notTaken = subsetSumRecursive(ind - 1, target, arr)
    taken = False
    if arr[ind] <= target:
        taken = subsetSumRecursive(ind - 1, target - arr[ind], arr)

    return notTaken or taken

def minSubsetSumDifferenceRecursive(arr):
    n = len(arr)
    totSum = sum(arr)
    possibleSums = []

    # Explore all subset sums from 0 to total sum
    for s in range(totSum + 1):
        if subsetSumRecursive(n - 1, s, arr):
            possibleSums.append(s)

    # Find the minimum difference between two subset sums
    mini = float('inf')
    for s in possibleSums:
        # (totSum - s) - s = totSum - 2 * s
        diff = abs(totSum - 2 * s)
        mini = min(mini, diff)

    return mini

# Memoization
'''Time Complexity: O(N*totSum) +O(N) +O(N)
Reason: There are two nested loops that account for O(N*totSum), 
at starting we are running a for loop to calculate totSum and at 
last a for loop to traverse the last row.

Space Complexity: O(N*totSum) + O(N)
Reason: We are using an external array of size ‘N * totSum’ and a 
stack space of O(N).
'''
def subsetSumUtil(ind, target, arr, dp):
    # Base case: If the target sum is 0, we have found a subset that sums to the target.
    if target == 0:
        return True

    # Base case: If we have reached the first element of the array, check if it equals the target.
    if ind == 0:
        return arr[0] == target

    # Check if the result for this combination of 'ind' and 'target' has already been computed.
    if dp[ind][target] != -1:
        return dp[ind][target]

    # Recursive cases:
    # 1. Try not taking the current element.
    notTaken = subsetSumUtil(ind - 1, target, arr, dp)

    # 2. Try taking the current element if it is less than or equal to the target.
    taken = False
    if arr[ind] <= target:
        taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)

    # Update the DP table and return the result.
    dp[ind][target] = notTaken or taken
    return dp[ind][target]

def minSubsetSumDifference(arr):
    n = len(arr)
    totSum = sum(arr)

    # Initialize a DP table to store the subset sum information.
    dp = [[-1 for i in range(totSum + 1)] for j in range(n)]

    # Calculate dummy values for all possible sums using subsetSumUtil.
    for i in range(totSum + 1):
        dummy = subsetSumUtil(n - 1, i, arr, dp)

    # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

    # Iterate through all possible sums.
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            # Calculate the difference between the current sum and the complement sum.
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini

# Tabulation
'''Time Complexity: O(N*totSum) +O(N) +O(N)
Reason: There are two nested loops that account for O(N*totSum), at starting 
we are running a for loop to calculate totSum, and at last a for loop to traverse the last row.

Space Complexity: O(N*totSum)
Reason: We are using an external array of size ‘N * totSum’. 
Stack Space is eliminated.'''
def minSubsetSumDifference(arr, n):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)

    # Initialize a DP table to store subset sum information.
    dp = [[False for i in range(totSum + 1)] for j in range(n)]

    # Initialize the base cases for the DP table.
    for i in range(n):
        dp[i][0] = True

    # Handle the base case for the first element in the array.
    if arr[0] <= totSum:
        dp[0][arr[0]] = True

    # Fill in the DP table using dynamic programming.
    for ind in range(1, n):
        for target in range(1, totSum + 1):
            # If the current element is not taken, the result is the same as the previous row.
            notTaken = dp[ind - 1][target]

            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = False
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]

            # Update the DP table with the result of taking or not taking the current element.
            dp[ind][target] = notTaken or taken

    # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

    # Iterate through all possible sums.
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            # Calculate the difference between the current sum and the complement sum.
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini