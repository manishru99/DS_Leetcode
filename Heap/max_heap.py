#Max Heap

class MaxHeap:
    def __init__(self):
        """Initialize an empty heap."""
        self.heap = []

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
        """Insert a new element into the heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        """Ensure the heap property is maintained after insertion."""
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        """Remove and return the largest element (root of the heap)."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Swap root with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        """Ensure the heap property is maintained after deletion."""
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def build_heap(self, array):
        """Transform an unsorted array into a valid max-heap."""
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def heap_sort(self):
        """Sort the elements using heap sort and return a sorted list."""
        sorted_list = []
        original_heap = self.heap[:]
        
        while self.heap:
            sorted_list.append(self.extract_max())

        self.heap = original_heap  # Restore original heap
        return sorted_list

    def get_heap(self):
        """Return the current heap as a list."""
        return self.heap

    def peek_max(self):
        """Return the maximum element without removing it."""
        return self.heap[0] if self.heap else None


# Example Usage
max_heap = MaxHeap()

# Insert elements into MaxHeap
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(2)
max_heap.insert(7)

print("MaxHeap after insertions:", max_heap.get_heap())  # Should be a valid max-heap
print("Extracted Max:", max_heap.extract_max())  # Should return 10
print("MaxHeap after extracting max:", max_heap.get_heap())

# Build heap from array
max_heap.build_heap([9, 4, 7, 1, 3, 6])
print("MaxHeap built from array:", max_heap.get_heap())

# Heap Sort
sorted_array_max = max_heap.heap_sort()
print("MaxHeap Sorted Array:", sorted_array_max)
