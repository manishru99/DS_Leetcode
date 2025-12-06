# 2158. Amount of New Area Painted Each Day

'''
There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [start_i, end_i]. This means that on the ith day you need to paint the area between start_i and end_i.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.
'''

def amountPainted(paint):
    # Find the farthest end point to size the painted array properly
    max_end = 0
    for interval in paint:
        if interval[1] > max_end:
            max_end = interval[1]
    # Initialize a boolean array to track painted positions on the number line
    painted = [False] * (max_end + 1)
    res = []  # Result list to store new area painted each day

    # Loop through each day's paint interval
    for start, end in paint:
        new_paint = 0 # Counter for how many new units we paint today

        # Iterate over the segment of the number line for the current day's interval
        for i in range(start, end):
            if not painted[i]:  # If this position hasn't been painted yet
                painted[i] = True  # Mark it as painted
                new_paint += 1      # Count it as newly painted

        res.append(new_paint)  # Store the result for this day

    return res
'''
Time Complexity
- Worst case: O(n × m) where n is number of days and m is the max interval length.
- Not ideal for large inputs, but great for understanding the problem.

'''