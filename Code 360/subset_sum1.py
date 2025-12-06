#Just print 1 subsequence whose sum is k and then stop.

def prints(ind, ds, s, sum, arr, n):
    """
    This function checks if a subset of the given array 'arr' sums up to the given 'sum'.

    Args:
        ind: The current index in the array.
        ds: A list to store the current subset.
        s: The current sum of the subset.
        sum: The target sum.
        arr: The input array.
        n: The length of the array.

    Returns:
        True if a subset with the given sum is found, False otherwise.
    """
    if ind == n:
        # If the current index is out of bounds:
        # Check if the current sum 's' matches the target 'sum'
        if s == sum:
            print(*ds)  # Print the subset
            return True
        else:
            return False

    # Include the current element 'arr[ind]' in the subset
    ds.append(arr[ind])
    s += arr[ind]

    # Recursively check if a subset with the given sum can be found 
    # by including the current element
    if prints(ind + 1, ds, s, sum, arr, n):
        return True

    # Exclude the current element from the subset
    s -= arr[ind]
    ds.pop()

    # Recursively check if a subset with the given sum can be found 
    # by excluding the current element
    if prints(ind + 1, ds, s, sum, arr, n):
        return True

    return False

# Example usage:
arr = [1, 2, 3]
n = len(arr)
sum = 3
ds = []  # Initialize an empty list to store the subset

if prints(0, ds, 0, sum, arr, n):
    print("Subset found")
else:
    print("Subset not found")