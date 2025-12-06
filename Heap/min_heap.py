import heapq

'''
Min Heap
used in real-world applications like priority queues, scheduling algorithms, and 
graph algorithms (Dijkstra's, Prim's).
'''

class MinHeap:
    def __init__(self):
        """Initialize an empty heap."""
        self.heap = []
        #self.index = 0

    def parent(self, i):
        """Return the index of the parent node."""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Return the index of the left child."""
        return 2 * i + 1
    
    def right_child(self, i):
        """Return the index of the right child."""
        return 2 * i + 2
    
    def insert(self, value):
        # TC = O(log n) SC = O(1)
        """Insert a new element into the heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        # TC O(log n)
        """Ensure the heap property is maintained after insertion."""
        """Move the element at index i up to its correct position."""
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # swap the parent and the child
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_min(self):
        # TC O(log n)
        """Remove and return the smallest element (root of the heap)."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Swap root with the last elem
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, i):
        # TC O(log n)
        """Ensure the heap property is maintained after deletion."""
        """Move the element at index i down to its correct position."""
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[i]: #first check with left child
            # left < len(self.heap) current node doesn’t have a left child, and we shouldn’t try to access it ie. the leaf nodes
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]: #check smallest with right child
            smallest = right
        if smallest != i:
            # swap the parent and the child
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def build_heap(self, array):
        # TC = O(n) SC = O(1)
        """Transform an unsorted array into a valid min-heap.
        Converts an unsorted array into a min-heap by applying _heapify_down() on all non-leaf nodes.
        starting from the last non-leaf node and moving up to the root."""
        self.heap = array
        for i in range(len(array) // 2, -1, -1):
            self._heapify_down(i)

    def heap_sort(self):
        #TC = O(n log n) SC = O(n)
        #ascending order output 
        """Sort the elements using heap sort and return a sorted list."""
        sorted_list = []
        original_heap = self.heap[:] #create a copy of the heap
        while self.heap:
            sorted_list.append(self.extract_min())

        self.heap = original_heap  # Restore original heap
        return sorted_list # ascending order o/p for min heap

    def get_heap(self):
        """Return the current heap as a list."""
        return self.heap

    def peek_min(self):
        """Return the minimum element without removing it."""
        return self.heap[0] if self.heap else None
    



# Example Usage
heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(3)
heap.insert(2)
heap.insert(7)

print("Heap after insertions:", heap.get_heap())  # Should be a valid min-heap

print("Extracted Min:", heap.extract_min())  # Should return 2
print("Heap after extracting min:", heap.get_heap())

# Build heap from array
heap.build_heap([9, 4, 7, 1, 3, 6])
print("Heap built from array:", heap.get_heap())

# Heap Sort
sorted_array = heap.heap_sort()
print("Heap Sorted Array:", sorted_array)
    