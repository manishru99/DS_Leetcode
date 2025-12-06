#90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #By bit manipulation
        n = len(nums)
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
Explanation
Sorting the List: Before adding the list to the set, we sort it to ensure that duplicate subsets are recognized as the same.
Converting List to Tuple: Since lists are not hashable, we convert the list to a tuple before adding it to the set.
Returning the Result: We convert the set of tuples back to a list of lists before returning the result.

'''