# 253  Meeting Rooms II

def minMeetingDays(intervals):
    if not intervals:
        return 0

    # Separate and sort start and end times
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)

    s = e = 0
    count = max_count = 0

    while s < len(start):
        if start[s] < end[e]:  # New meeting overlaps
            count += 1
            max_count = max(max_count, count)
            s += 1
        else:  # Meeting has ended, free a slot
            count -= 1
            e += 1

    return max_count
'''
     Time Complexity: O(n log n)
Where n is the number of meetings.
- Sorting start and end arrays → O(n log n)
- Iterating through start with pointer s → O(n)
- Each pointer moves at most n times, so total traversal cost is linear after sorting.
✅ Total time: O(n log n) due to sorting.

🧠 Space Complexity: O(n)
- start and end arrays each use O(n) space.
- Constant extra space for pointers and counters.
✅ Total space: O(n)

'''

# Greedy + Heap

import heapq

def minMeetingDays(intervals):
    if not intervals:
        return 0

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Min-heap to track end times of current day's meetings
    heap = []

    for meeting in intervals:
        start, end = meeting

        # Free up a day if the previous meeting ended before or at current start
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        # Allocate this meeting to a day (new or reused)
        heapq.heappush(heap, end)

    return len(heap)

'''
In this min-heap approach, we store the end times of currently active meetings in the heap.
Why?
Because the heap helps us track the earliest meeting that finishes, which lets us decide:
- If the current meeting can reuse that time slot (i.e. it starts at or after the earliest end time → pop from heap)
- Or if it needs a new slot/day (i.e. it overlaps → push another end time into the heap)
So at any moment, the number of entries in the heap reflects how many meetings are overlapping, or in your context — the minimum number of days needed.

'''
