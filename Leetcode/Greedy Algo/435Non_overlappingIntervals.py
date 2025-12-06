#From Leetcode 75

#Greedy
# Method 1
#TC = O(nlogn) + O(n) = O(nlogn)
# SC = O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1: return 0
        #intervals.sort(key=lambda x: x[0])  #sort intervals list
        intervals.sort()   #O(nlogn)
        i = 0
        count = 0

        while i < n-1:   #O(n)
            if intervals[i][1] > intervals[i+1][0]: #end of i > start of i+1 it means overlapping
                intervals[i+1][1] = min(intervals[i][1], intervals[i+1][1])
                count += 1 
            i += 1
        return count


'''
Resolving Overlaps:
If there's an overlap, the second interval (intervals[i+1]) is updated to have the smaller of the two end times (min(intervals[i][1], intervals[i+1][1])). This ensures that the interval with the smaller end time is preserved, minimizing the chance of future overlaps.
The count variable is incremented to track the number of intervals removed.


IMP:

Why Sorting Intervals is O(n log n):
When you call intervals.sort() or intervals.sort(key=lambda x: x[0]), Python sorts the list of intervals by the specified key (default: first element of each subarray).
Sorting a list of n intervals requires Python to:
Divide the list into smaller parts (like in merge sort), which requires log(n) steps.
Merge and compare the intervals in each step, requiring O(n) comparisons for each level of merging.
Combining these steps gives the total time complexity of O(n log n).


''' 

# Method 2 Greedy
# TC = O(nlogn) + O(n) = O(nlogn)
# SC = O(1)

# Logic of max num of meetings (n meetings 1 room)

def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # Step 1: Sort the intervals by their ending times (second element).
    # This helps prioritize intervals with the smallest end time for non-overlapping selection.
    intervals.sort(key=lambda x: x[1])
    
    # Step 2: Initialize a counter for overlapping intervals and track the last non-overlapping interval's end time.
    cnt = 0
    last = intervals[0][1]  # Start by considering the end time of the first interval.
    
    # Step 3: Iterate through the sorted intervals, starting from the second interval.
    for i in range(1, len(intervals)):  # 'len(intervals)' is the total number of intervals.
        if intervals[i][0] >= last:  
            # If the current interval's start time is greater than or equal to the end time of
            # the last non-overlapping interval, update 'last' to the current interval's end time.
            last = intervals[i][1]
        else:
            # If the current interval overlaps with the last non-overlapping interval,
            # increment the overlap counter as this interval cannot be selected.
            cnt += 1
    
    # Step 4: Return the count of overlapping intervals that need to be removed.
    return cnt