#Takes an elem and places/inserts it in it's correct position/order

# Logic: 
# Insertion sort builds a sorted array one element at a time
# by repeatedly taking the next element and inserting it into 
# the correct position in the already sorted part of the array.

# Start with the 2nd elem, 1st elem is considered sorted for 1 size array. 
# Then arr size 2, compare it with 1st
# Then arr size 3, compare it with 2nd and then 1st
# And so on until the last elem is reached.
# The arr is divided into 2 parts: sorted and unsorted.

#TC = O(n^2)  (worst and avg case)
#TC = O(n)    (Best case)  

def insertion_sort(arr, n):
    # The outer loop should start from i = 1 instead of i = 0 
    # since the first element is already considered sorted in insertion sort.
    for i in range(1, n):
        j=i
        # Move elements of arr[0..i-1], that are greater than arr[i], to one position ahead
        # if arr is already sorted while just checks once and exists
        # This happens as we forward by forming a sorted portion of the arr from start
        while( j>0 and arr[j-1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
            print("Runs")
        
    return arr

n = int(input("Size: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))

print("Array before sorting: ")
for i in range(n):
    print(arr[i])

arr = insertion_sort(arr, n)

print("Array after sorting: ")
for i in range(n):
    print(arr[i])



