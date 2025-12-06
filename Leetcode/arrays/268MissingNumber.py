#268. Missing Number
'''
Method 1:
#TC = O(n)
#SC = O(1)
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    array_sum = sum(nums)  # Sum of elements in the array
    return total_sum - array_sum  # The missing number
'''

def missingNumber(self, nums: List[int]) -> int:
        
    #Method 2
    #TC = O(3n)
    #SC = O(n)
    entries = {} #hashmap dict
    #nums.sort()
    n = len(nums)

    for i in range(n+1):
        entries[i] = 0

    for num in nums:
        entries[num] = 1  #If elem exists in nums enter 1 in hashmap
    
    #By list comprehension
    #return next(key for key, val in entries.items() if val == 0)
    
    for key, val in entries.items():
        if val == 0:
            return key
        
        