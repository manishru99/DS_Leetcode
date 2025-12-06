# 994. Rotting Oranges

from collections import deque

def oranges_rotting(grid):
    # Edge case: empty grid
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    count_fresh = 0 # Total number of fresh + rotten oranges

    # Step 1: Add all initially rotten oranges to the queue
    # Count all non-empty cells (fresh + rotten)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))
            if grid[i][j] != 0:
                count_fresh += 1

    # If no fresh oranges present then directly return 0
    if count_fresh == 0:
        return 0

    count_min = 0 # Minutes passed
    cnt = 0  # Total number of oranges processed (rotted)
    dx = [0, 0, 1, -1] # row movement
    dy = [1, -1, 0, 0]  # col movement 

    # Step 2: BFS from initially rotten oranges
    while queue:
        size = len(queue) # Number of oranges to process this minute
        cnt += size  # Update count of processed oranges

        for _ in range(size):
            x, y = queue.popleft() # Current rotten orange position
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                # Skip out-of-bound or empty or already rotten cells
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != 1:
                    continue
                # Rot the fresh orange and add to queue
                grid[nx][ny] = 2
                queue.append((nx, ny))
        # If queue is not empty, increment time
        if queue:
            count_min += 1
    return count_min if count_fresh == cnt else -1

'''- If all fresh oranges were processed (count_fresh == cnt), return the minutes taken.
- Otherwise, return -1 to indicate not all oranges could rot.
'''
