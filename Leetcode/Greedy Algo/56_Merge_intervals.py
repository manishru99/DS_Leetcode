# 56. Merge Intervals

# Ask the interviewer if the given i/p intervals are sorted?

# TC = O(nlogn) + O(2n)
'''
Time Complexity: O(n²) in the worst case
Here’s why:
- The outer loop runs n times.
- The inner loop (starting from i+1) can also, in the worst case, run up to n−i times per iteration.
- In the worst-case scenario — where no intervals are completely disjoint — this results in quadratic behavior.
So the overall time complexity is O(n²).
'''
# SC = O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals based on the start value
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = []
        # Step 2: Iterate through the sorted intervals
        for i in range(len(intervals)):
            start = intervals[i][0]  # Start of the current interval
            end = intervals[i][1] # End of the current interval

            # Step 3: If the last interval in `ans` fully covers the current interval, skip it
            '''This early skip is intended to avoid re-processing an interval that is completely 
            covered by a previously merged one (already in ans)'''
            if ans and ans[-1][1] >= end:
                continue
            # Step 4: Merge overlapping intervals
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= end: # If the next interval starts before the current one ends
                    end = max(end, intervals[j][1]) # Extend the end of the merged interval
                else:
                    break # Stop merging when intervals no longer overlap
            # Step 5: Append the merged interval to the result list
            ans.append([start, end])
        return ans

# Solution 2
# TC = O(nlogn) + O(n)
# SC = O(n)

# This version uses a greedy, in-place merge strategy and guarantees O(n log n) time due to sorting, followed by a single linear pass

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = []
        for i in range(len(intervals)):
            # If ans is empty or there is no overlap with the previous interval
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            # Overlapping intervals: update the end time of the last merged interval
            else:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
        return ans

