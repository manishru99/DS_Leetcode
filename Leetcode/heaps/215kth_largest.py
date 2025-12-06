# 215. Kth Largest Element in an Array

# Method 1 Sorting:
# TC = O(n log n)
# SC = O(1) or O(n)
'''
Used nums1 to store the sorted arr in desc order 
As we shouldn't modify the originAL arr
'''
def findKthLargest(self, nums: List[int], k: int) -> int:
    nums1 = sorted(nums, reverse = True)
    return nums1[k-1]



# Method 2: Max heap (Neetcode heap sol)
'''
TC = O(n) + O(n) + O(k log n) = O(n + k log n)
- heapify is linear time.
- Each of the k heappop operations takes O(logn) because the heap shrinks gradually.

SC: O(n)
Max Heap: The space required to store the heap is (O(n)), as it contains all the elements of the input list.
Auxiliary Space: The space used by the list comprehension and the heapify operation is (O(n)).
'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Negate for max heap
        max_heap = [-num for num in nums]  #O(n)
        heapq.heapify(max_heap) #O(n)
        # Pop k times
        for _ in range(k): #O(k)
            elem = -heapq.heappop(max_heap) #O(log n)
        # kth time popped elem is kth largest
        return elem
    
# Solution 2 Using Min-heap (Maintain heap of size k)
# Dry run: nums = [3,2,1,5,6,4], k = 2
'''
 How It Works
- Maintain a min-heap of the k largest elements seen so far.
- If the heap exceeds size k, we pop the smallest — this keeps the top-k largest.
- At the end, the smallest in the heap is the kth largest overall.

- Push 3 → [3]
- Push 2 → [2, 3] (heap auto-sorts)
✅ Heap size is now k, so from now on:
- Push 1
→ heap: [1, 3, 2] → too big, pop 1 → heap becomes [2, 3]
- Push 5
→ heap: [2, 3, 5] → pop 2 → [3, 5]
- Push 6
→ heap: [3, 5, 6] → pop 3 → [5, 6]
- Push 4
→ heap: [4, 6, 5] → pop 4 → [5, 6]

 Time Complexity: O(nlogk)
- You iterate through all n elements in nums.
- Each heappush and (optional) heappop operation takes O(logk) time since the heap size is at most k.
- So, for n elements:
→ O(nlogk) total time
This is faster than sorting the full list (O(nlogn)), especially when k is small.

Space Complexity: O(k)
- The heap only stores the k largest elements at any time.
- No extra space beyond this (excluding input list).
'''
import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


# Method 3
# Using Priority Queue (min heap)
'''
TC = O(n log k)
SC = O(k)
Use a Min-Heap: Maintain a min-heap of size k. 
The root of the heap will always be the k-th largest element.
Iterate Through the Array: For each element in the array, push it onto the heap. 
If the heap size exceeds k, pop the smallest element (the root) to maintain the heap size.
'''
def findKthLargest(self, nums: List[int], k: int) -> int:
    # Create a min-heap with the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Iterate through the remaining elements
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
    
    # The root of the heap is the k-th largest element
    return min_heap[0]

# More readable code for above method 2
import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Build a min-heap with the first k elements
        min_heap = []
        for num in nums[:k]:
            heapq.heappush(min_heap, num) # O(logk)

        # Step 2: Process the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappop(min_heap)      # Remove the smallest
                heapq.heappush(min_heap, num)  # Push the new candidate

        # Step 3: The root of the heap is the k-th largest
        return min_heap[0]

# Method 3 Quick select (unoptimized)  USE THIS
'''
Time Complexity
- Average case: O(n)
- Each partition splits the array, and we only recurse into one side.
- On average, the pivot divides the array evenly, so the work reduces geometrically.
- Worst case: O(n²)
- Happens when the pivot is consistently the smallest or largest element (e.g., already sorted array with poor pivot choice).
- You can mitigate this by using a randomized pivot.

Space Complexity
- O(1) auxiliary space (in-place partitioning)
- O(log n) recursive stack space in average case
- O(n) recursive stack space in worst case (deep recursion)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert k-th largest to k-th smallest index (0-based)
        k = len(nums) - k

        def quickSelect(l, r):
            # Choose the rightmost element as pivot
            pivot, p = nums[r], l

            # Partition the array: elements <= pivot to the left
            for i in range(l, r): # i goes from l to r - 1 
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # Place pivot in its correct position
            nums[p], nums[r] = nums[r], nums[p]

            # Recursively search in the appropriate partition
            if p > k:
                return quickSelect(l, p - 1)  # Search left
            elif p < k:
                return quickSelect(p + 1, r)  # Search right
            else:
                return nums[p]  # Found the k-th smallest (i.e., k-th largest)

        # Start Quick Select on the full array
        return quickSelect(0, len(nums) - 1)
'''
Quick Select is typically designed to find the k-th smallest element in an array using 0-based indexing. So:
- The smallest element is at index 0
- The 2nd smallest is at index 1
- …
- The k-th smallest is at index k - 1
But when you're asked to find the k-th largest, you're actually looking for the element at index:
len(nums) - k
This is because:
- Sorting the array in ascending order puts the largest at the end.
- So the k-th largest is the same as the (n - k)-th smallest.

'''

# Method 4 Quick select (optimized)
class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        # Choose the middle element and swap it with the element next to left
        mid = (left + right) >> 1
        nums[mid], nums[left + 1] = nums[left + 1], nums[mid]

        # Perform median-of-three pivot selection to improve partition quality
        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] < nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] < nums[left + 1]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]

        # Use the adjusted middle value as pivot
        pivot = nums[left + 1]
        i = left + 1
        j = right

        # Partition the array around the pivot
        while True:
            # Move i rightward until we find an element <= pivot
            while True:
                i += 1
                if not nums[i] > pivot:
                    break
            # Move j leftward until we find an element >= pivot
            while True:
                j -= 1
                if not nums[j] < pivot:
                    break
            # If pointers cross, partitioning is complete
            if i > j:
                break
            # Swap out-of-place elements
            nums[i], nums[j] = nums[j], nums[i]

        # Place pivot in its correct position
        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j  # Return final index of pivot

    def quickSelect(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1

        while True:
            # Handle small subarray directly
            if right <= left + 1:
                if right == left + 1 and nums[right] > nums[left]:
                    nums[left], nums[right] = nums[right], nums[left]
                return nums[k]  # Return the k-th largest (adjusted index)

            # Partition the array and get pivot index
            j = self.partition(nums, left, right)

            # Narrow the search space based on pivot position
            if j >= k:
                right = j - 1
            if j <= k:
                left = j + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert k-th largest to k-th index in 0-based sorted array
        return self.quickSelect(nums, k - 1)
    

# Method x
#The findKth smallest function uses a Quickselect algorithm, 
# which is similar to Quicksort
def findKthLargest(self, nums: List[int], k: int) -> int:
    left = 0
    right = len(nums) - 1
    kth = 0
    while True:
        # Partition the array and get the index of the pivot element
        idx = self.partition(nums, left, right)
        # If the pivot index is the k-1 position, we found the kth largest element
        if idx == k - 1:
            kth = nums[idx]
            break
        # If the pivot index is less than k-1, search in the right part of the array
        if idx < k - 1:
            left = idx + 1
        # If the pivot index is greater than k-1, search in the left part of the array
        else:
            right = idx - 1
    return kth

def partition(self, arr: List[int], left: int, right: int) -> int:
    pivot = arr[left] # Choose the pivot element
    l = left + 1  # Start from the element next to the pivot
    r = right  # Start from the end of the array
    while l <= r:
        # Swap elements to ensure all elements less than pivot are on the left
        # and all elements greater than pivot are on the right
        if arr[l] < pivot and arr[r] > pivot:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        # Move the left pointer to the right if the current element is greater than or equal to the pivot
        if arr[l] >= pivot:
            l += 1
        # Move the right pointer to the left if the current element is less than or equal to the pivot
        if arr[r] <= pivot:
            r -= 1
    # Place the pivot element in its correct position
    arr[left], arr[r] = arr[r], arr[left]
    return r # Return the index of the pivot element

'''
TC = O(n) (avg TC)
TC = O(n^2) (worst case)
SC = O(1)
The average time complexity of Quickselect is O(n), where n is the number of elements in the array. This is because, on average, each partition step reduces the problem size by half.

However, in the worst case, the time complexity can be O(n^2). This happens when the pivot selection is poor, and the partitioning does not effectively reduce the problem size (e.g., always picking the smallest or largest element as the pivot).
'''