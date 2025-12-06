# 41. First Missing Positive

#Solution 1
# TC = O(nlogn) + O(3n) = O(nlogn)  the sorting step, dominates the other operations.
#here n belongs to the set [1, len(nums)+1] 1 when 1 is not in the list and len(nums)+1 when all the nums are in the list
# SC = O(n)
'''
def firstMissingPositive(self, nums: List[int]) -> int:
    # Filter out non-positive numbers
    nums = [num for num in nums if num > 0] #O(n) SC = O(n)
    # Remove duplicates
    nums = list(set(nums))  #O(n)  
    nums.sort() #O(nlogn) SC = O(n)
    cnt = 1
    for num in nums: #O(n)
        if num == cnt:
            cnt += 1
        else:
            break
    return cnt
    '''

#Solution 2
#Using a set to store nums (hashset)
#TC = O(n) SC = O(n)
'''
def firstMissingPositive(self, nums: List[int]) -> int:
    nums1 = set(nums) #O(n) SC = O(n)
    cnt = 1
    while cnt in nums1:  #O(n)
        cnt += 1
    return cnt
'''

#Solution 3
# Using the array itself as a hashset
#Here too the values are changed to negative to show that the num exists
#TC = O(n + n + n) = O(n)
#SC = O(1)

def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)
    # Replace negative numbers and zeros with a number greater than n
    for i in range(n):
        if nums[i] <= 0: 
            nums[i] = n + 1

    # check val is betw [1 to n]
    # and check val at it's (val-1) pos of num is >=0
    # then make it -ve to show it exists

    #Skip for -ve as it means that it's a duplicate and already exists

    # if val is n, then it's index is n-1
    # Mark the presence of numbers in the range [1, n]
    
    for i in range(n):
        val = abs(nums[i])
        if 1 <= val <= n:
            if nums[val - 1] > 0:
                nums[val - 1] *= -1

    # check for +ve entry which is the 1st missing +ve
    for i in range(n):
        if nums[i] > 0:
            return i+1
    return n+1

'''
Note: Why do we check if the value is between 1 to n? Logic? (In this:  if 1 <= val <= n:)
Range of Interest: The problem is to find the smallest missing positive integer. The smallest positive integers are in the range from 1 to ( n ) (where ( n ) is the length of the list). Any number outside this range (e.g., negative numbers, zeros, or numbers greater than ( n )) cannot be the smallest missing positive integer.
Marking Presence: By checking if 1 <= val <= n, we ensure that we only mark the presence of numbers that are within the range of interest. If a number is within this range, we mark its presence by making the value at the corresponding index negative. For example, if val = 3, we mark the presence of 3 by making nums[2] (index 2) negative.
Ignoring Irrelevant Values: Numbers outside the range of 1 to ( n ) are irrelevant for the purpose of finding the smallest missing positive integer. By ignoring these values, we avoid unnecessary operations and focus only on the relevant numbers.
'''

#Method 4
#Cyclic sort
'''
#TC = O(n) SC = O(1)
The first for loop runs n times.
Inside this loop, the while loop ensures that each element is swapped to its correct position. In the worst case, each element is swapped at most once, leading to a linear number of swaps.
The second for loop also runs n times.
Since each element is processed a constant number of times, the overall time complexity is O(n).
modifying the input array nums in place. The idea is to put each num in its correct position. so SC = O(1)
'''

def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        #3 conditions
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1
