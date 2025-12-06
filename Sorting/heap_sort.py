# Heap Sort

# TC = O(nlogn) SC = O(1)
def heapify(arr, n, i):
    largest = i         # Assume current node is largest
    left = 2 * i + 1    # Left child
    right = 2 * i + 2   # Right child

    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the current node, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Step 1: Build max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # Swap max element to the end
        heapify(arr, i, 0)                # Heapify reduced heap

    return arr