# 46 Permutations

# Given a collection of distinct numbers, return all possible permutations.
#Solution 1
#TC = O(n*n!)
#SC = O(n*n!) space dominated by the answer list

class Solution:

    ans = []
    ds = []
    
    def recurPermute(self, nums: List[int], freq: List[int]):
        # Base case: If the length of the temporary list `ds` is equal to nums, we have found a permutation
        if len(self.ds) == len(nums):
            self.ans.append(self.ds.copy())  # Store a copy of the valid permutation
            return

        # Try adding each element in nums that hasn't been used yet
        for i in range(len(nums)):
            if not freq[i]:  # If the element at index `i` has not been used
                self.ds.append(nums[i])  # Add it to our current permutation
                freq[i] = 1  # Mark it as used
                
                # Recur to generate the next element in the permutation
                self.recurPermute(nums, freq)
                
                # Backtrack: Remove the last element and mark it as unused
                freq[i] = 0
                self.ds.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []  # Reset answer list
        self.ds = []   # Reset temporary storage list
        freq = [0] * len(nums)  # Frequency array to track used elements
        
        self.recurPermute(nums, freq)  # Start recursion
        return self.ans  # Return all stored permutations
'''
Lists ans and ds:
ans stores all permutations, and in the worst case, it will store (n!) permutations, each of length (n). So, the space used by ans is (O(n \cdot n!)).
ds is a temporary list used to build permutations, and its maximum length is (n). So, the space used by ds is (O(n)).
Frequency array freq:
This array has a fixed size of (n), so its space complexity is (O(n)).
Recursive call stack:
The depth of the recursion is (n), so the space used by the call stack is (O(n)).
Combining these, the overall space complexity is dominated by the space required to store all permutations in ans, which is (O(n \cdot n!)).
'''