# 79. Word Search

# For Explanation rfr CodewithAryan YT

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Keep track of visited cells to avoid reusing them
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, index):
            # Base case: All characters matched
            if index == len(word):
                return True

            # Boundary check and constraints
            if not (0 <= r < rows and 0 <= c < cols):
                return False  # Out of bounds
            if visited[r][c]:
                return False  # Already used in current path
            if board[r][c] != word[index]:
                return False  # Character does not match

            # Mark current cell as visited
            visited[r][c] = True

            # Explore in all 4 directions (up, down, left, right)
            if (dfs(r - 1, c, index + 1) or  # Up
                dfs(r + 1, c, index + 1) or  # Down
                dfs(r, c - 1, index + 1) or  # Left
                dfs(r, c + 1, index + 1)):   # Right
                return True  # If any path returns true, word is found

            # Backtrack: unmark visited cell
            visited[r][c] = False
            return False  # No valid path from this cell

        # Try to find the starting point for DFS
        for r in range(rows):
            for c in range(cols):
                # Start DFS only if the first character matches
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False  # Word not found in any path

'''
TC = O(m × n × 4^L)

In the worst case, you may start a DFS from every cell in the board ⇒ O(m × n).
From each cell, the DFS explores up to 4 directions (up/down/left/right) recursively.
DFS continues for up to L characters (length of the word).
Since each path must not reuse the same cell, the effective branching factor is at most 3 after the first move (can't revisit the previous cell), but for complexity analysis, we approximate it as 4^L.

SC = O(m × n + L)
The space complexity is O(m × n) for the visited matrix and O(L) for the recursion stack in the worst case.

Key Concepts Used in Your Solution
DFS (Depth-First Search) to explore all valid paths from a cell.

Backtracking to revert changes (unmark visited) when a path doesn’t lead to a solution.

Visited Matrix to track cells already used in the current path to avoid cycles.

Logic
Start DFS from each cell that matches the first character of word.

Recursively check adjacent cells for the next character.

Use a visited matrix to ensure no cell is reused in the current path.

If the entire word is found (index == len(word)), return True.

Use backtracking to revert the state when needed.


'''