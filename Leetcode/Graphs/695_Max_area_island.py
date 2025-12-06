# 695. Max Area of Island

from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Function to find the largest island area in a given grid.
        Uses BFS to explore connected land cells and calculate island size.

        Parameters:
        - grid: 2D binary matrix (1 represents land, 0 represents water).

        Returns:
        - Maximum area of an island (integer).
        """
        
        if not grid:
            return 0  # Return 0 if the grid is empty
        
        # Get dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Visited array to track explored cells
        vis = [[False] * n for _ in range(m)]
        max_area = 0  # Variable to store the largest island found
        
        def bfs(row, col):
            """
            BFS traversal to explore an island and compute its area.
            """
            queue = deque([(row, col)])  # Initialize queue for BFS
            vis[row][col] = True  # Mark the starting cell as visited
            area = 0  # Initialize island area
            
            # Direction vectors for moving up, left, down, right
            del_row = [-1, 0, 1, 0]  
            del_col = [0, -1, 0, 1]  
            
            while queue:
                r, c = queue.popleft()  # Get the front cell from queue
                area += 1  # Increment island area
                
                # Explore all 4 neighboring directions
                # check all the next level nodes 
                for i in range(4):
                    new_r, new_c = r + del_row[i], c + del_col[i]
                    
                    # Check if new coordinates are within bounds and valid
                    if (
                        0 <= new_r < m and 0 <= new_c < n and  # Grid boundaries
                        not vis[new_r][new_c] and grid[new_r][new_c] == 1  # Land cell and unvisited
                    ):
                        vis[new_r][new_c] = True  # Mark as visited
                        queue.append((new_r, new_c))  # Add to queue for further exploration
            
            return area  # Return the computed island area
        
        # Iterate through the grid and start BFS for each unvisited land cell
        for r in range(m):
            for c in range(n):
                if not vis[r][c] and grid[r][c] == 1:  # If cell is unvisited and land
                    max_area = max(max_area, bfs(r, c))  # Get maximum island area
        
        return max_area  # Return the maximum island size found
    
'''
Time Complexity:
- Each cell in the grid is processed once, either as part of an island (via BFS) 
or skipped if it's water (0).
- BFS traversal visits each cell only once, marking it as visited.
- Since each edge in the grid connects land cells O(m × n) in total, 
the overall TC is O(m × n).

Space Complexity:
- Visited array (vis): Takes O(m × n) space.
- Queue (deque) for BFS storage: In the worst case (a single large island), the queue can grow up to O(m × n).
- Other auxiliary variables (loop counters, direction vectors): O(1).
Thus, overall space complexity is O(m × n).

'''