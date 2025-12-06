# 1055. Shortest Way to Form String
# https://algo.monster/liteproblems/1055

'''
Greedy two-pointer solution

We repeatedly scan through the source string using a pointer, and in 
each scan, match as much of the target string as we can (in order). 
Each full scan over source counts as one subsequence.
'''
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, count = 0, 0  # i -> index in target, count -> subsequence count

        while i < len(target):
            j = 0  # for source scan
            old_i = i  # To check if any progress is made

            while j < len(source) and i < len(target):
                if source[j] == target[i]:
                    i += 1  # matched character, move both pointers
                j += 1  # always move in source

            if i == old_i:
                # No progress made in this scan: character not in source
                return -1

            count += 1  # one subsequence used

        return count
'''
Time Complexity: O(m × n)
Where:
- m is the length of the target string
- n is the length of the source string
In the worst case, each character in target may require scanning the entire source to find a match:
- If target = "aaaaa" and source = "bcdef" → you'll scan source repeatedly for each unmatched a.
So in the worst case:
Time = O(m × n)
SC = O(1)
'''

# Greedy + HashMap with Binary Search
# Above sol is good
'''
Strategy Overview
Instead of scanning the source string every time, we preprocess it into a map:
Each character points to a sorted list of indices where it appears in the source.
Then, for each character in target, we use binary search to find the next valid occurrence beyond the current position.
This way, we scan the target only once and jump efficiently through source
'''
from collections import defaultdict
import bisect

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Step 1: Map each character to its positions in source
        pos_map = defaultdict(list)
        for i, ch in enumerate(source):
            pos_map[ch].append(i)

        count = 1      # At least one pass over source
        idx_in_source = -1  # Pointer in source (starts before the beginning)

        for ch in target:
            if ch not in pos_map:
                return -1  # Can't match character at all

            idx_list = pos_map[ch]
            # Binary search for the smallest index > idx_in_source
            i = bisect.bisect_right(idx_list, idx_in_source)
            if i == len(idx_list):
                # No valid next index — need a new pass
                count += 1
                idx_in_source = idx_list[0]
            else:
                idx_in_source = idx_list[i]

        return count
    
'''
- Preprocessing: O(n) where n = len(source)
- For each target character:
- Binary search: O(log k) where k = number of times that character appears in source
- So overall: O(m × log n) for m = len(target)
🧠 Space Complexity:
- O(n) for the position map

'''