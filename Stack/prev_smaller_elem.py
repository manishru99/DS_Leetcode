# Previous Smaller Element

# Given an array, find the previous smaller element for every element in the array. 
# If there is no previous smaller element on the left hand side, print -1.

def previous_smaller_element(arr):
    st = []
    # Initialize result with -1 (default if no smaller element exists)
    res = [-1] * len(arr)
    # Traverse the array from left to right
    for i in range(len(arr)):
        # Maintain an increasing stack
        while st and st[-1] >= arr[i]:
            st.pop()
        if st:
            res[i] = st[-1]
        st.append(arr[i])
    return res
        
# Example usage
arr = [3, 1, 2, 4]
print(previous_smaller_element(arr)) # o/p: [-1, -1, 1, 2]