# Heap using Priority Queue 

# Min Heap

from queue import PriorityQueue

# Create an empty Min-Heap
min_heap = PriorityQueue()

# Insert elements into Min-Heap
#O(log n)
min_heap.put(10)
min_heap.put(5)
min_heap.put(15)
min_heap.put(1)

#removes and returns an item from the queue
# (ie. remove and return lowest priority item from the queue)
#min_heap.get()

# Extract elements in sorted order (ascending)
while not min_heap.empty():
    print(min_heap.get(), end=" ")  # Output: 1 5 10 15
print()

#Deletion of an elem
#O(log n)
min_heap.get()


# Max Heap

from queue import PriorityQueue

# Create an empty Max-Heap
max_heap = PriorityQueue()

# Insert elements into Max-Heap (using negative values)
max_heap.put(-10)
max_heap.put(-5)
max_heap.put(-15)
max_heap.put(-1)

# Extract elements in sorted order (descending)
while not max_heap.empty():
    print(-max_heap.get(), end=" ")  # Output: 15 10 5 1
print()
