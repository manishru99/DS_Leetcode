# Previous Greater Element

# Given an array of integers, find the nearest previous greater element for every element in the array. 
# If there is no greater element, print -1.

# TC = O()

def previous_greater_element(arr):
    st = []
    res = [-1] * len(arr)
    # Traverse the array from left to right
    for i in range(len(arr)):
        # Maintain a decreasing stack
        while st and st[-1] <= arr[i]:
            st.pop()
        if st:
            res[i] = st[-1]
        st.append(arr[i])
    return res

# Example usage
arr = [3, 1, 2, 4]
print(previous_greater_element(arr)) # o/p: [-1, 3, 3, -1]
