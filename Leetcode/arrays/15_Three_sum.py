# 15. 3Sum

# Brute 
# TC = O(n^3) SC = O(m)
# Where m is the number of triplets and n is the length of the given array.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()           # Use a set to store unique triplets
        nums.sort()           # Sort the array to help with duplicate handling

        # Brute-force approach: iterate over all possible triplet combinations
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    # Check if the sum of the triplet is zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        tmp.sort()             # Sort the triplet so duplicates can be caught by the set
                        res.add(tuple(tmp))    # Add the triplet as a tuple to ensure uniqueness

        return [list(i) for i in res]  # Convert tuples back to lists for the final output
    
# using hashset
'''
# Time Complexity: O(n²)
- The outer loop runs n times.
- For each iteration of the outer loop, the inner loop runs approximately n - i times.
- Within the inner loop:
- Lookup and insert operations in the hash set are O(1) on average.
- Sorting a fixed-length list of three elements is O(1).
- Overall, this results in O(n²) time complexity.
🔁 Compared to the brute-force triple-nested loop O(n³) approach, this is significantly more efficient.

🧠 Space Complexity: O(n + m)
- O(n) for the hash set used during each outer iteration (seen), which at most holds up to n elements.
- O(m) for the final result set res, where m is the number of unique valid triplets.
🧮 Final output space depends on the number of unique combinations found, but the auxiliary space for hash sets keeps it linear.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()              # Sort to handle duplicates and two-pointer logic
        res = set()              # Use a set to avoid duplicate triplets
        n = len(nums)

        for i in range(n):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip current iteration

            seen = set()         # HashSet to store complements
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in seen:
                    triplet = tuple(sorted([nums[i], nums[j], third]))
                    res.add(triplet)
                seen.add(nums[j])  # Track values we've seen so far

        return [list(t) for t in res]


# Two pointer approach
# TC = O(NlogN)+O(N2)
# SC = O(no. of quadruplets)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()             # nlogn Sort the array to enable two-pointer approach and handle duplicates
        res = []                # Result list to store unique triplets
        n = len(nums)

        # Iterate through the array, treating nums[i] as the first element of the triplet
        for i in range(n): # O(n)
            # Skip duplicate values to avoid duplicate triplets starting with the same nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1   # Initialize two pointers: one from the left of remaining subarray, one from the right

            # Use two-pointer technique to find pairs whose sum with nums[i] is zero
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    # If sum is too small, move left pointer to the right to increase the sum
                    j += 1
                elif total_sum > 0:
                    # If sum is too large, move right pointer to the left to decrease the sum
                    k -= 1
                else:
                    # Found a valid triplet that sums to zero
                    temp = [nums[i], nums[j], nums[k]]
                    res.append(temp)

                    # Move both pointers inward to look for new pairs
                    j += 1
                    k -= 1

                    # Skip duplicates for the second value to avoid repeating triplets
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicates for the third value
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res