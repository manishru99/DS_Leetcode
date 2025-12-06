# 763. Partition Labels

'''
Time complexity: O(2n) = O(n)
Space complexity: O(m)
Where n is the length of the string s and 
m is the number of unique characters in the string s. Basically SC = O(26) = O(1)
'''

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Given a string `s`, partitions the string into as many parts as possible 
        so that each letter appears in at most one part, and returns a list of sizes of these parts.
        """

        last_ind = {}  # Step 1: Hashmap to store the last occurrence of each character
        for i, c in enumerate(s):
            last_ind[c] = i  # Updates the last occurrence index for each character

        res = []  # Step 2: List to store partition sizes
        size = 0  # Tracks the size of the current partition
        end = 0  # Tracks the farthest last occurrence in the current partition

        for i, c in enumerate(s):
            size += 1  # Increment partition size
            end = max(end, last_ind[c])  # Extend partition to include last occurrence of current character
            
            if i == end:  # If we reach the end of a partition
                res.append(size)  # Store partition size
                size = 0  # Reset size for the next partition

        return res  # Return list of partition sizes