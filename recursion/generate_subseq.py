# Power Set: Print all the possible subsequences of the String

# Using recursion
def generate_subsequences(sequence, index = 0, current_subsequence=None, result=None):
    if result is None:
        result = []
    if current_subsequence is None:
        current_subsequence = []

    #base case: if we've reached the end of the sequence
    if(index == len(sequence)):          
        result.append(current_subsequence)
        return result
    
    #include
    generate_subsequences(sequence, index+1, current_subsequence + [sequence[index]], result)

    #Exclude 
    generate_subsequences(sequence, index+1, current_subsequence, result)         

    return result

sequence = [1, 2, 3]
subsequences = generate_subsequences(sequence)
print(subsequences)


'''
Time Complexity Analysis
The function explores all possible subsequences of sequence, meaning it considers both:
- Including an element.
- Excluding an element.
For a sequence of length n, each element has two choices (include or exclude), leading to a binary recursion tree with 2^n nodes.
📌 Time Complexity: O(2^n)
This represents the exponential growth due to all possible subsets being generated.

Space Complexity Analysis
- Recursive Call Stack
- Since recursion goes depth n, the maximum stack frames is O(n).
- Result Storage (result)
- The function stores all subsequences, which means it holds O(2^n) elements in the worst case.
📌 Space Complexity: O(2^n)
This accounts for both result storage and recursive stack depth.

'''