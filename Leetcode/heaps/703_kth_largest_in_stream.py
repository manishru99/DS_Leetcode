# 703. Kth Largest Element in a Stream

import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums  # Store elements in a min-heap to keep track of the k largest
        self.k = k
        heapq.heapify(self.minHeap)  # Heapify to maintain the heap property (min-heap)

        # Ensure the heap only has k elements by removing the smallest ones
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # Add the new value to the heap

        # If heap grows beyond size k, remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The root of the min-heap is the kth largest element
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
Initialization (__init__):
- heapify(self.minHeap): O(n), where n is the number of elements in nums
- while len(self.minHeap) > k: each heappop is O(logn), and runs at most n - k times
So overall:
- Worst case total time for __init__: O(n + (n - k) logn)
Adding a value (add method):
- heappush: O(logk)
- Potential heappop (if heap exceeds size k): O(logk)
- So each add operation is: O(logk)
'''

# Brute force Rfr Neetcode
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]
    
'''
- Since the list is sorted in ascending order:
- The last element is the largest → index len(self.nums) - 1
- The k-th largest is at index len(self.nums) - k
- self.nums[len(self.nums) - self.k]
Returns the value at that index — the k-th largest element.
'''