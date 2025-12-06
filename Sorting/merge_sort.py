# Merge Sort (Divide and Conquer)

'''Merge Sort is a divide-and-conquer algorithm that:

1. Divides the array into two halves recursively until each 
subarray has one element.
2. Merges the sorted subarrays back together in order.
Each merge step combines two sorted arrays into one, maintaining order. 
It has a consistent time complexity of O(nlogn) and uses O(n) space 
due to the extra arrays during merging.
'''
#TC = O(nlogn)   
#SC = O(n) 
def merge_sort(arr, low, high):
    #base case
    #In order to stop recursion we write a base case
    if( low >= high ):
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)   
    return arr

def merge(arr, low, mid, high):
    temp = [] #create empty temp arr
    left = low      #starting index of left half of arr
    right = mid + 1 #starting index of right half of arr

    #Start storing elem in temp arr in sorted order
    while( left<=mid and right<=high):
        if( arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
        
    #Add remianing elem from left half if any
    while(left <= mid):
        temp.append(arr[left])
        left += 1
    #Add remianing elem from right half if any
    while(right <= high):
        temp.append(arr[right])
        right += 1
    
    #Copy elem from temp back to arr in original pos
    for i in range(low, high+1):
        arr[i] = temp[i-low]

n = int(input("Size: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))

print("Array before sorting: ")
for i in range(n):
    print(arr[i])

arr = merge_sort(arr, 0, n-1)

print("Array after sorting: ")

for i in range(n):
    print(arr[i])


   
