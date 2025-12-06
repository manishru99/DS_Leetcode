# 907. Sum of Subarray Minimums

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # brute force
        '''
        n = len(arr)
        MOD = 10**9 + 7
        subarr = []
        #generate all subarr
        for i in range(n):
            for j in range(i, n):
                subarr.append(arr[i: j+1])
        # iterate over subarr list and find min from all subarrays
        min_list = []
        for i in range(len(subarr)):
            min_list.append(min(subarr[i]))
        return (sum(min_list)) % (10**9 + 7)
        
        #solution 2:
        # TC = O(n^2)
        # SC = O(1)
        MOD = 10**9 + 7
        n = len(arr)
        result = 0

        # Iterate over all subarrays
        for i in range(n):
            curr_min = float('inf')  # Initialize the current minimum for the subarray
            for j in range(i, n):
                curr_min = min(curr_min, arr[j])  # Update the minimum for the current subarray
                result = (result + curr_min) % MOD  # Add the minimum to the result (modulo 10**9 + 7)
        return result
        '''


