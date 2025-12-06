#Selection sort selects the minimum and brings to the front
#Keywords: Minimum Front

# We are dividing the array into two subparts: one sorted and one unsorted.
# In each iteration, we find the minimum element from the unsorted part and swap it with the first unsorted element.
# In this way the sorted part goes on increasing and unsorted decreasing

#TC = O(n^2)
#As for each outer loop iteration, the inner loop runs for n-i-1 times
# = n + n-1 + n-2 + ...
#SC = O(1)

def selection_sort(arr, n):
    #2 pointers
    #1 for the element to be checked
    #And other from i+1 to n
    for i in range(n-1): # 0 to n-2
        #for each iteration ith index is considered min at first
        min_index = i 
        for j in range(i+1, n): # 1 to n-1
            if(arr[j] < arr[min_index]):
                min_index = j
        #move min element to it's correct position
        if min_index != i:  # Avoid unnecessary swaps
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    
    '''
    #2nd approach using while loop
    i=0
    while(i<n):
        for j in range(i+1, n):
            if(arr[i] >= arr[j]):
                #Swap
                arr[i], arr[j] = arr[j], arr[i]
        i+=1
    return arr
    '''

n = int(input("Size: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))

print("Array before sorting: ")
for i in range(n):
    print(arr[i])

arr = selection_sort(arr, n)

print("Array after sorting: ")
for i in range(n):
    print(arr[i])


