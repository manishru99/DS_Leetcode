# N meetings in one room

# 252 Meeting Rooms 1 (Similar)

# TC = O(n + nlogn) = O(nlogn)
# SC = O(3n) + O(k) = O(3n) + O(n) = O(n)
# k is the number of selected meetings in worst case k = n

class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos
        
class Solution:
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, start, end):
        n = len(start)
        # Creating a list of meeting objects.
        meet = [meeting(start[i], end[i], i + 1) for i in range(n)]
        # Sorting the meetings by end time first and by position as tie-breaker.
        meet = sorted(meet, key=lambda x: (x.end, x.pos)) # O(nlogn)
        
        # Initializing the limit as the end time of the first meeting
        limit = meet[0].end
        # List to store the positions of selected meetings
        answer = []
        answer.append(meet[0].pos)
        
        for i in range(1, n):  # O(n)
            # Check if the next meeting's start time is greater than the last selected meeting's end time
            if meet[i].start > limit:
                limit = meet[i].end
                answer.append(meet[i].pos)
        
        # Return the number of meetings that can be accommodated
        return len(answer)

# Example usage:
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
solution = Solution()
print(solution.maximumMeetings(start, end))  # Output: 4