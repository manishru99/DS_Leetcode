# Heap implementation using built-in functions

import heapq

# Min Heap

# Create an empty Min-Heap
min_heap = []

# Insert elements into Min-Heap
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 1)

# Print Min-Heap (Heap is stored as an array)
print("Min-Heap:", min_heap)  # Output: [1, 5, 15, 10]

# Get the minimum element (without removing)
print("Peek Min:", min_heap[0])

# Extract the minimum element
min_element = heapq.heappop(min_heap)
print("Extracted Min:", min_element)  # Output: 1
print("Min-Heap after extraction:", min_heap)

# Convert an unsorted array into a Min-Heap
# Heapify the array in-place
array = [9, 4, 7, 1, 3, 6]
heapq.heapify(array)
print("Min-Heap built from array:", array)  # Output: [1, 3, 6, 4, 9, 7]

# Heap Sort using Min-Heap
sorted_list = [heapq.heappop(array) for _ in range(len(array))]
print("Sorted List using Min-Heap:", sorted_list)  # Output: [1, 3, 4, 6, 7, 9]




# Max Heap

# Create an empty Max-Heap
max_heap = []

# Insert elements into Max-Heap (Negating values)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -15)
heapq.heappush(max_heap, -1)

# Convert back to positive to see the heap
print("Max-Heap:", [-x for x in max_heap])  # Output: [15, 10, 5, 1]

# Get the maximum element (without removing)
print("Peek Max:", -max_heap[0])  # Output: 15

# Extract the maximum element
max_element = -heapq.heappop(max_heap)
print("Extracted Max:", max_element)  # Output: 15
print("Max-Heap after extraction:", [-x for x in max_heap])  # Output: [10, 1, 5]

# Convert an array into a Max-Heap
array = [9, 4, 7, 1, 3, 6]
#list comprehension that creates a new list, max_heap, where each element is the negation of the corresponding element in the original array
max_heap = [-x for x in array]  # o/p = arr1 = [-9, -4, -7, -1, -3, -6]
heapq.heapify(max_heap)
print("Max-Heap built from array:", [-x for x in max_heap])  # Output: [9, 4, 7, 1, 3, 6]

# Heap Sort using Max-Heap
sorted_list = [-heapq.heappop(max_heap) for _ in range(len(max_heap))]
print("Sorted List using Max-Heap:", sorted_list)  # Output: [9, 7, 6, 4, 3, 1]


'''
TC:
Insert: O(log n)
Extract: O(log n)
Peek: O(1)
Heapify: O(n)


heapify():

Remove the smallest element: The smallest element (root of the heap) is removed.
Replace the root: The last element in the heap is moved to the root position.
Heapify down: The heap is restructured to maintain the heap property by calling the 
_siftup() method, which ensures that the new root element is moved to its correct position in the heap.


heappush():

Append the new element: The new element is appended to the end of the heap (which is represented as a list).
Heapify up: The new element is then moved up the heap to its correct position to maintain the heap property. This process is also known as “sifting up” or “percolating up”.

heapify():

Input List: The input list is passed to the heapify() function.
Initialization: The input list is initialized with the given elements.
Heapify Process:
The function starts from the last non-leaf node and moves upwards to the root.
For each node, it calls the _siftup() method (also known as _heapify_down()), which ensures that the subtree rooted at that node satisfies the heap property.
Maintain Heap Property: The _siftup() method swaps elements if they are not in their correct position, ensuring that the parent node is less than or equal to its child nodes (for a min-heap).
'''