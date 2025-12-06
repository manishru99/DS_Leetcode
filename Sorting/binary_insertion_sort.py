# Binary Insertion Sort

'''
Binary insertion sort is a sorting algorithm which is similar to the 
insertion sort, 
but instead of using linear search to find the location where an element 
should be inserted, we use binary search. 
Thus, we reduce the comparative value of inserting a single element from 
O (N) to O (log N).
'''

def binary_insertion_sort(arr):
    def binary_search(subarr, val, start, end):
        while start <= end:
            mid = (start+end)//2
            if subarr[mid] < val: # val lies on right
                start = mid + 1
            else:
                end = mid - 1
        return start
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i-1)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr

print("Sorted array:")
print(binary_insertion_sort([37, 23, 0, 31, 22, 17, 12, 72, 31, 46, 100, 88, 54]))

'''
TC:
- Traditional insertion sort takes O(n²) time due to linear search.
- Binary Insertion Sort reduces comparison time to O(log n) using binary search.
- But shifting elements still takes O(n), so overall time complexity remains O(n²) in the worst case.
SC:
This creates new slices and concatenates them — which temporarily generates new lists during each iteration. So:
- Worst-case Space Complexity: O(n²) due to repeated list copying for each insertion.
'''

# In-place version
# Built-in list methods pop() and insert()
def binary_insertion_sort_inplace(arr):
    def binary_search(arr, val, start, end): # we find the start in the main arr only
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] < val:
                start = mid + 1
            else:
                end = mid - 1
        return start

    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, key, 0, i - 1)
        arr.pop(i)
        arr.insert(pos, key)

    return arr
'''
- Time Complexity: O(n²)
- Space Complexity: O(1) auxiliary (in-place)
'''