#iterative binary search (using while loop)
#TC = O(log n)
#SC = O(1)
def binary_search_iterative(arr, target):
    """
    Perform a binary search for the target value in the sorted list using an iterative approach.

    Parameters:
    arr (list): The sorted list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        #naive formula:
        #can cause integer overflow if low and high are large numbers
        #mid = (low + high) // 2
        #For Overflow case:
        mid = low + (high - low)//2
        #Python handles large integers natively, so overflow isn’t a concern
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

#Recursive Binary Search
#TC = O(log n)
#SC = O(log n)
#Recursive implementations of binary search can take O(log n) 
# space due to the recursion stack.
#For an array of size n, the number of divisions is log2n, 
# which determines the maximum depth of the recursion stack.

def binary_search_recursive(arr, target, low, high):
    # base
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example usage:
if __name__ == "__main__":
    my_list = [10, 23, 45, 70, 80, 100]
    target_value = 70

    result = binary_search_iterative(my_list, target_value)
    if result != -1:
        print(f"Element found at index {result+1}")
    else:
        print("Element not found in the list")

    result1 = binary_search_recursive(my_list, target_value, 0, len(my_list) - 1)
    if result1 != -1:
        print(f"Element found at index {result+1}")
    else:
        print("Element not found in the list")