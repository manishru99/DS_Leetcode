#90. Subsets II

#Recursive solution

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #By bit manipulation
        n = len(nums)
        '''
        subsets = 1<<n
        ans = set()
        for num in range(subsets):
            lst=[]
            for i in range(n):
                #Check ith bit is set or no
                if num & (1<<i):
                    lst.append(nums[i])
            # Convert list to tuple before adding to set
            ans.add(tuple(sorted(lst)))
        # Convert set of tuples back to list of lists
        return [list(i) for i in ans]
        '''

        #By recursion
        ans = []  # Stores the final list of unique subsets
        ds = []   # Temporary list to build subsets

        def findSubsets(ind: int):
            ans.append(ds[:])  # Append a copy of ds (current subset) to ans

            #Base case: When ind == n we don't enter the loop
            for i in range(ind, len(nums)):
                # Skip duplicate elements to avoid duplicate subsets
                if i != ind and nums[i] == nums[i - 1]:
                    continue
                ds.append(nums[i])   # Include current element in the subset
                findSubsets(i + 1)    # Recursive call to explore further
                ds.pop()              # Backtrack (remove last element)

        nums.sort()  # Sort the array to ensure duplicates are adjacent
        findSubsets(0)  # Start recursive function from index 0
        return ans

'''
Time Complexity: O(2^n) for generating every subset and O(k)  to insert every subset in another 
data structure if the average length of every subset is k. Overall O(k * 2^n).

Space Complexity: O(2^n * k) to store every subset of average length k. 
Auxiliary space is O(n)  if n is the depth of the recursion tree.
'''

