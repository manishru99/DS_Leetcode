# 252 Meeting Rooms 1

def canAttendMeetings(intervals):
    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Check for overlaps
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False  # Overlap found
    return True
