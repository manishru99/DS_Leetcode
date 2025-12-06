# 239. Sliding Window Maximum

# Brute
'''
TC = O(n*k) n is len(nums), k is window size
SC = O(n)
You're storing one maximum value per window in ans_max
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans_max = []
        for i in range(len(nums) - k + 1):
            max_elem = nums[i]
            for j in range(i, i + k):
                max_elem = max(nums[j], max_elem)
            ans_max.append(max_elem)
        return ans_max
    
# Sliding window

# stack and queue playlist striver
from collections import deque
def maxSlidingWindow(nums, k):
    n = len(nums)
    result = []
    q = deque()  # Stores indices of useful elements in window

    for i in range(n):
        # Remove elements out of the current window
        # if left val of window becomes out of bounds ie size of the window should be 3
        if q and q[0] == i - k:  # q[0] -> q [front]
            q.popleft()  # pop from front

        # While q is non empty and the top val in our q or the rightmost val 
        # is less than the val we are inserting that is the i val
        # Remove smaller elements in k range as they are not useful
        while q and nums[q[-1]] < nums[i]:
            q.pop()       # pop from rear
        # Only after we do the above we append the i ind from rear
        q.append(i)

        # Append current max to result once window is at least size k
        if i >= k - 1:
            result.append(nums[q[0]])  # val at q[front] which is the max

    return result

# Test example
arr = [4, 0, -1, 3, 5, 3, 6, 8]
k = 3
print(f"Maximum element in every {k} window:")
print(maxSlidingWindow(arr, k))

'''
Time Complexity: O(N) + O(n) = O(2n) 
n for for loop and we are pushing maximum n elem and taking out same n elem so n

Space Complexity: O(K) for the queue + O(n-k) for storing the ans
'''