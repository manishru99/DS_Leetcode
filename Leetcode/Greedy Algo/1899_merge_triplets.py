# 1899. Merge Triplets to Form Target Triplet

# TC = O(n) SC = O(1)

from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        Determines if it is possible to form the 'target' triplet 
        using elements from valid triplets.

        Args:
        triplets (List[List[int]]): List of triplets, each containing three integers.
        target (List[int]): Desired triplet to form.

        Returns:
        bool: True if the target triplet can be formed, otherwise False.
        """

        good = set()  # Set to store indices that match the target values

        for t in triplets:
            # Step 1: Filter out triplets that exceed target values
            # If any value in the triplet exceeds the corresponding value in the target triplet, ignore it
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue  # Skip this triplet, as it cannot contribute to forming the target

            # Step 2: Check for elements that match the target triplet
            for ind, val in enumerate(t):  
                if val == target[ind]:  # If a value matches its corresponding index in the target
                    good.add(ind)  # Add the index to the 'good' set

        # Step 3: Verify if all three indices (0, 1, 2) are present in the set
        # If we have matched all elements of the target triplet, return True
        return len(good) == 3