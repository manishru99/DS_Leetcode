# 200. Number of Islands

from collections import deque  # Import deque for BFS traversal
# 4 directional sol
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  # Edge case: If the grid is empty, return 0
            return 0
        
        # Get grid dimensions
        m = len(grid)
        n = len(grid[0])
        
        # Create a visited array to track visited cells
        vis = [[False] * n for _ in range(m)]
        num_islands = 0  # Counter to track the number of islands

        # BFS function to explore the connected component (island)
        def bfs(row, col):
            queue = deque([(row, col)])  # Initialize queue with the starting cell
            vis[row][col] = True  # Mark starting cell as visited
            
            # Directions for moving up, down, left, and right
            del_row = [-1, 0, 1, 0]  # delta row
            del_col = [0, -1, 0, 1]  # delta col

            while queue:  # Continue until all connected land cells are explored
                r, c = queue.popleft()  # Get the front cell from the queue
                
                # Check all four possible directions
                for i in range(4):
                    new_r, new_c = r + del_row[i], c + del_col[i]

                    # Ensure the new position is within bounds and not visited
                    if 0 <= new_r < m and 0 <= new_c < n and not vis[new_r][new_c] and grid[new_r][new_c] == "1":
                        vis[new_r][new_c] = True  # Mark as visited
                        queue.append((new_r, new_c))  # Add to queue for further exploration

        # Iterate through the grid
        for r in range(m):
            for c in range(n):
                # If cell is unvisited & land, it represents a new island
                if not vis[r][c] and grid[r][c] == "1":
                    num_islands += 1  # Increment island count
                    bfs(r, c)  # Perform BFS to explore the entire island

        return num_islands  # Return the total number of islands
    
'''
The del_row and del_col arrays define the relative movement directions for traversing a 2D grid in four possible directions:
- Up: Move one row up → (-1, 0)
- Left: Move one column left → (0, -1)
- Down: Move one row down → (1, 0)
- Right: Move one column right → (0, 1)

Time Complexity Analysis:
- We iterate through the entire grid, checking each cell once → O(n*m).
- If a land cell ('1') is found, we initiate BFS traversal:
- Each BFS call explores an entire island by visiting all connected '1' cells.
- Since every cell is visited exactly once, the total BFS traversal is O(n * m).
Thus, the overall time complexity is O(n * m), where n is the number of rows and m is the number of columns.

Space Complexity Analysis:
- Visited matrix (vis): Takes O(n × m) space for tracking visited cells.
- Queue (deque) for BFS: In the worst case (a single large island), the queue can grow up to O(n × m).
- Other auxiliary variables take O(1) space.
Thus, the overall space complexity is O(n × m).

'''

# 8-directional

from collections import deque

class Solution:
    def bfs(self, row, col, vis, grid):
        vis[row][col] = 1
        q = deque()
        q.append((row, col))
        
        n = len(grid)
        m = len(grid[0])
        
        while q:
            r, c = q.popleft()
            # Traverse all 8 neighbors (including diagonals)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nrow, ncol = r + dr, c + dc
                    if (0 <= nrow < n and 0 <= ncol < m and 
                        grid[nrow][ncol] == '1' and not vis[nrow][ncol]):
                        vis[nrow][ncol] = 1
                        q.append((nrow, ncol))

    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        cnt = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1' and not vis[row][col]:
                    cnt += 1
                    self.bfs(row, col, vis, grid)

        return cnt
    
# the 2 for loops create this:
'''
Together, this creates 9 combinations:
(-1,-1) (-1,0) (-1,1)
( 0,-1) ( 0,0) ( 0,1)
( 1,-1) ( 1,0) ( 1,1)
'''



