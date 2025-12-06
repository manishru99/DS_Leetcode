# Quick Sort (Divide and Conquer) Rfr striver from 15:00
'''Quick Sort is a divide-and-conquer algorithm that works by:

1. Choosing a pivot element from the array.
2. Partitioning the array so that:
   - Elements less than the pivot go to the left
   - Elements greater go to the right
3. Recursively applying the same logic to the left and right subarrays.

Its efficient with an average time complexity of O(nlog n) and 
worst-case O(n²) (if pivot choice is poor). 
Randomized pivot selection helps avoid the worst case.
'''
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            pi = self.partition(arr, low, high) #pi is partition index
            # left subarr
            self.quickSort(arr, low, pi - 1)
            # right subarr
            self.quickSort(arr, pi + 1, high)
    
    def partition(self,arr,low,high):
        pivot = arr[low] # Choosing 1st elem as the pivot
        i = low
        j = high
        while i < j:
            # check 1
            # if the num at i is bigger than pivot then problematic else increment i
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            # check 2
            # if the num at j is smaller than pivot then problematic else decrement j
            while arr[j] >= pivot and j >= low + 1:
                j -= 1
            # IMP:
            # Reason for high -1 and low + 1, if the arr is sorted then the elem left
            # and right of pivot are already sorted, when we end above while loops,
            # the i and j points to the same elem which is the pivot
            # i and j swapped with itself
            # And below i swapped with pivot itself 
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            # if i has crossed j then exit from this loop and swap (outer while loop)
        # place pivot at its correct pos by swapping with j
        arr[low], arr[j] = arr[j], arr[low]
        return j # return pivot as the partition index and sort the left
        # and right side recursively
    

'''
TC:
Best Case: O(nlogn)
This occurs when the pivot element is always the middle element, leading to balanced partitions.

Average Case: O(nlogn)
On average, the pivot will partition the array into two nearly equal halves.

Worst Case: O(n2)
This happens when the pivot is always the smallest or largest element, leading to highly unbalanced partitions 
(e.g., when the array is already sorted).

SC:
In-Place Version: O(logn)
This is due to the recursive stack space used during the sorting process.

Non In-Place Version: O(n)
If additional arrays are used for partitioning, the space complexity increases.
'''