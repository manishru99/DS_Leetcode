#We can solve this by setting and unsetting the bits.
#For [1,2,3] 0th, 1st, 2nd bit and form 2^3 subsequences/subsets
def subsets(self, nums: List[int]) -> List[List[int]]:
    #Bit manipulation sol
    #eg. nums = [1,2,3]
    n = len(nums)        #n = size of list
    subsets = 1<<n  #num of subsets
    #Run a loop from 0 to subsets-1
    #eg. from 0 to 7
    ans = []
    for num in range(0, subsets):  #O(2**n)
        lst = []
        for i in range(0, n):      #O(n)
            #Check if ith bit is set or not
            if(num & (1<<i)):
                lst.append(nums[i])
        ans.append(lst)
    return ans

#TC = O(n x 2**n)
#SC = O(n x 2**n)  (approx)

'''
Explanation:
Sure! Let's break down the code step by step to understand how it generates all possible subsets (the power set) of a given integer array `nums` using bit manipulation.

### Explanation

1. **Initialization:**
   ```python
   n = len(nums)
   subsets = 1 << n  # Number of subsets (i.e., 2^n)
   ans = []
   ```
   - `n` is the length of the input array `nums`.
   - `subsets` is calculated as `1 << n`, which is equivalent to \(2^n\). This represents the total number of possible subsets.
   - `ans` is an empty list that will store all the subsets.

2. **Generating Subsets:**
   ```python
   for num in range(0, subsets):
       lst = []
       for i in range(0, n):
           # Check if ith bit is set or not
           if(num & (1 << i)):
               lst.append(nums[i])
       ans.append(lst)
   ```
   - The outer loop runs from `0` to `subsets - 1` (i.e., from `0` to \(2^n - 1\)). Each value of `num` represents a unique combination of elements in the subset.
   - For each `num`, an empty list `lst` is initialized to store the current subset.
   - The inner loop runs from `0` to `n - 1`. For each bit position `i`, it checks if the `i`-th bit of `num` is set (i.e., `1`).
     - The expression `(num & (1 << i))` checks if the `i`-th bit of `num` is set. If it is, the corresponding element `nums[i]` is added to the current subset `lst`.
   - After processing all bits, the current subset `lst` is added to the list of all subsets `ans`.

3. **Returning the Result:**
   ```python
   return ans
   ```
   - Finally, the list `ans` containing all possible subsets is returned.

### Example

Let's go through an example with `nums = [1, 2, 3]`:

- `n = 3`, so `subsets = 1 << 3 = 8`. There are 8 possible subsets.
- The outer loop runs from `0` to `7` (binary representations: `000` to `111`).

For each value of `num`:
- `num = 0` (binary `000`): No bits are set, so the subset is `[]`.
- `num = 1` (binary `001`): Only the 0th bit is set, so the subset is `[1]`.
- `num = 2` (binary `010`): Only the 1st bit is set, so the subset is `[2]`.
- `num = 3` (binary `011`): The 0th and 1st bits are set, so the subset is `[1, 2]`.
- `num = 4` (binary `100`): Only the 2nd bit is set, so the subset is `[3]`.
- `num = 5` (binary `101`): The 0th and 2nd bits are set, so the subset is `[1, 3]`.
- `num = 6` (binary `110`): The 1st and 2nd bits are set, so the subset is `[2, 3]`.
- `num = 7` (binary `111`): All bits are set, so the subset is `[1, 2, 3]`.

The final result is:
```
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

This approach ensures that all possible subsets are generated without duplicates.
'''




        