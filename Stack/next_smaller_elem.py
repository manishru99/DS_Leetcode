# Next Smaller Element

def next_smaller_element(arr):
    st = []
    res = [-1] * len(arr)

    # Traverse the array from right to left
    for i in range(len(arr)-1, -1, -1):
        # Maintain an increasing stack
        while st and st[-1] >= arr[i]:
            st.pop()
        if st:
            res[i] = st[-1]
        st.append(arr[i])
    return res

# Example usage
arr = [4, 1, 2]
print(next_smaller_element(arr)) # o/p: [1, -1, -1]
