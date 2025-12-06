# 57. Insert Interval

# TC = O(n)
# SC = O(n) for res arr

def insert(intervals, new_interval):
    n = len(intervals)
    result = []

    for i in range(n):
        # If the new interval ends before the current interval starts
        # right part
        if new_interval[1] < intervals[i][0]:
            result.append(new_interval)
            # Add the remaining intervals from the array
            # As we are sure that the next intervals will be after the curr interval
            # which is after the newInterval
            result.extend(intervals[i:]) # extend: extend list by appending elements from the iterable.
            return result
        
        # If the current interval ends before the new interval starts
        # left part
        elif intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
        else:
            # Overlapping intervals, merge them to create a new interval
            # Merge intervals by updating the start and end of the new interval
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])

    # Add the last merged interval
    result.append(new_interval)
    return result