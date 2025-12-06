
'''
Steps to Perform Binary Search
- Treat the 2D array as a 1D array:- Total number of elements = rows * cols.
- Flatten the 2D array into a logical 1D array by treating index mid = (low + high) // 2 as:- Row index = mid // cols.
- Column index = mid % cols.

- Compare the element at the computed index with the target.
- Adjust the low and high pointers based on the comparison.
'''


def binarySearch2D(matrix, target):
    if not matrix or not matrix[0]:  # Check for an empty matrix
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1  # Treat it as a flattened array

    while low <= high:
        mid = (low + high) // 2
        row, col = mid // cols, mid % cols  # Map 1D index to 2D indices
        mid_element = matrix[row][col]

        if mid_element == target:
            return True  # Target found
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return False  # Target not found

# Example Usage:
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
target = 9
print(binarySearch2D(matrix, target))  # Output: True