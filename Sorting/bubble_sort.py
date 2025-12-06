# push the max to the last by adjacent swaps
# Keywords: Maximum Last

#TC = O(n^2)
#But Best case TC = O(n)

def bubble_sort(arr, n):
    
    #outer loop runs from end to 1st index
    for i in range(n-1, 0, -1):  # just running loop from last else can follow below another approach
        swapped = False
        #inner loop runs from 0 index to i-1 
        for j in range(0, i):
            # Compare adjacent elements
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        #print("runs")     
        #TO see how many time runs for 
        #determining best TC

        # If no two elements were swapped by inner loop, the array is sorted
        if not swapped:
            break
        #This optimization can improve the TC in the best case to O(n) when the array is already sorted
        #while the worst-case time complexity remains O(n^2)
        '''
        # Another approach
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]    
        '''
    return arr

n = int(input("Size: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))

print("Array before sorting: ")
for i in range(n):
    print(arr[i])

arr = bubble_sort(arr, n)

print("Array after sorting: ")
for i in range(n):
    print(arr[i])









