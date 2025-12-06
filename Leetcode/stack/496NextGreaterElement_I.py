# Basic NGE implementation

'''finding the next greater element for each index in a linear array 
(non-circular version). You're using a monotonic stack that works backwards
through the array to maintain a decreasing sequence.
'''
# TC = O(n) Each element is pushed and popped at most once
# SC = O(n)
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        nge = [-1] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                nge[i] = st[-1]
            st.append(nums[i])
        return nge
    
# Circular version
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        nge = [-1] * n
        st = []
        for i in range(2 * n - 1, -1, -1):
            idx = i % n # use idx inplace of i % n everywhere
            while st and st[-1] <= nums[idx]:
                st.pop()
            # i < n is used so that in 1st iteration of the arr we only update the 
            # st for nge for the last elem since this is a circular arr
            # and dpn't update nge[]
            if i < n:
                if st:
                    nge[i] = st[-1]
            st.append(nums[idx])
        return nge




# MONOTONIC STACK:
#When we store elements in a specific order in a stack either in increasing or decresing that is when we call
#it as a monotonic stack

# The monotonic stack is a data structure that is used to maintain a monotonic sequence of elements.
# A monotonic stack can be either increasing or decreasing, depending on the problem requirements.
# The key idea behind the monotonic stack is to maintain a stack of elements such that the elements are either in increasing or decreasing order.
# This allows us to efficiently find the next greater or smaller element for each element in the input array.
# The monotonic stack is commonly used in problems that require finding the next greater or smaller element for each element in an array.


# The idea is to use a stack to maintain a decreasing subsequence of elements from the input array nums2.
# We iterate through nums2 in reverse order and maintain a decreasing stack.
# For each element num in nums2, we pop elements from the stack until we find an element greater than num.
# The next greater element for num is the top element of the stack.
# If the stack is empty, there is no greater element for num.
# We store the next greater element for each element in nums2 in a dictionary next_greater.
# Finally, we create the result array for nums1 based on the next greater elements found in nums2.
# The time complexity of this approach is O(nums1.length + nums2.length), where nums1 and nums2 are the input arrays.
# The space complexity is O(nums2.length) for the dictionary next_greater and the stack.

# Optimized
#TC = O(nums1.length + nums2.length)

def next_greater_element(nums1, nums2):
    #Create a dictionary next_great to store the NGE for each number in nums2 for constant-time lookup. O(1)
    #Hashing
    next_greater = {}
    stack = []

    # Iterate through nums2 in reverse order
    for num in reversed(nums2):
        # Maintain a decreasing stack
        while stack and stack[-1] <= num: #stack here is not empty is also checked as It ensures that the stack is not empty before accessing its top element. This is necessary to avoid an IndexError when trying to access st[-1] if the stack is empty.
            stack.pop()
        # If stack is not empty, the top element is the next greater element
        if stack:
            next_greater[num] = stack[-1]  #Update dict
        else:
            next_greater[num] = -1         #Update dict
        # Push the current element onto the stack
        stack.append(num)

    # Create the result array for nums1 based on the next greater elements found in nums2
    result = [next_greater[num] for num in nums1]

    return result

# Example usage
nums1 = [4, 1, 2]  #nums1 is a subset of nums2 and we need to find the nge of nums1 in nums2
nums2 = [1, 3, 4, 2]
print(next_greater_element(nums1, nums2))  # Output: [-1, 3, -1]


# Brute
#TC = O(nums1.length * (nums2.length)^2)
#SC = O(nums1.length)

def next_greater_element_brute_force(nums1, nums2):
    result = []
    for num1 in nums1:
        found = False
        for i in range(len(nums2)):
            if nums2[i] == num1:
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > num1:
                        result.append(nums2[j])
                        found = True
                        break
                if not found:
                    result.append(-1)
                break
    return result

# Example usage
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater_element_brute_force(nums1, nums2))  # Output: [-1, 3, -1]

